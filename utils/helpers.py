import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import os

def display_image_safely(image_path, caption="", width=None):
    """Safely display image with error handling"""
    try:
        if os.path.exists(image_path):
            img = Image.open(image_path)
            st.image(img, caption=caption, width=width)
        else:
            st.warning(f"Image not found: {image_path}")
    except Exception as e:
        st.error(f"Error loading image: {e}")

def create_india_map(state_tourism_df):
    """Create an interactive choropleth map of India with tourism data"""

    # State name mapping for GeoJSON compatibility
    state_name_mapping = {
        'Andhra Pradesh': 'Andhra Pradesh',
        'Arunachal Pradesh': 'Arunachal Pradesh',
        'Assam': 'Assam',
        'Bihar': 'Bihar',
        'Chhattisgarh': 'Chhattisgarh',
        'Goa': 'Goa',
        'Gujarat': 'Gujarat',
        'Haryana': 'Haryana',
        'Himachal Pradesh': 'Himachal Pradesh',
        'Jharkhand': 'Jharkhand',
        'Karnataka': 'Karnataka',
        'Kerala': 'Kerala',
        'Madhya Pradesh': 'Madhya Pradesh',
        'Maharashtra': 'Maharashtra',
        'Manipur': 'Manipur',
        'Meghalaya': 'Meghalaya',
        'Mizoram': 'Mizoram',
        'Nagaland': 'Nagaland',
        'Odisha': 'Odisha',
        'Punjab': 'Punjab',
        'Rajasthan': 'Rajasthan',
        'Sikkim': 'Sikkim',
        'Tamil Nadu': 'Tamil Nadu',
        'Telangana': 'Telangana',
        'Tripura': 'Tripura',
        'Uttar Pradesh': 'Uttar Pradesh',
        'Uttarakhand': 'Uttarakhand',
        'West Bengal': 'West Bengal',
        'Andaman and Nicobar Islands': 'Andaman & Nicobar Island',
        'Chandigarh': 'Chandigarh',
        'Dadra and Nagar Haveli and Daman and Diu': 'Dadara & Nagar Havelli',
        'Delhi': 'Delhi',
        'Jammu and Kashmir': 'Jammu & Kashmir',
        'Ladakh': 'Ladakh',
        'Lakshadweep': 'Lakshadweep',
        'Puducherry': 'Puducherry'
    }

    # Prepare map data with total tourism for 2022+2023
    map_data = []
    for idx, row in state_tourism_df.iterrows():
        state_name = row['STATE']
        total_tourism_2_years = row['YEAR_2022'] + row['YEAR_2023']
        growth = ((row['YEAR_2023'] - row['YEAR_2022']) / row['YEAR_2022']) * 100 if row['YEAR_2022'] > 0 else 0

        map_data.append({
            'State': state_name,
            'State_Mapped': state_name_mapping.get(state_name, state_name),
            'Tourism_2023': row['YEAR_2023'],
            'Tourism_2022': row['YEAR_2022'],
            'Total_Tourism_2Years': total_tourism_2_years,
            'Growth': growth,
            'Region': row['REGION']
        })

    if map_data:
        map_df = pd.DataFrame(map_data)

        # Create choropleth map using built-in India geojson
        try:
            fig = px.choropleth(
                map_df,
                locations='State_Mapped',
                color='Total_Tourism_2Years',
                hover_name='State',
                hover_data={
                    'Tourism_2023': ':,.1f',
                    'Tourism_2022': ':,.1f',
                    'Total_Tourism_2Years': ':,.1f',
                    'Growth': ':+.1f%',
                    'Region': True,
                    'State_Mapped': False
                },
                color_continuous_scale='Greens',
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                projection='mercator',
                title='🗺️ India Tourism Map - Total Tourist Arrivals (2022 + 2023)',
                labels={
                    'Total_Tourism_2Years': 'Total Tourists (M)',
                    'Tourism_2023': '2023 Arrivals (M)',
                    'Tourism_2022': '2022 Arrivals (M)',
                    'Growth': 'Growth Rate (%)'
                }
            )

            # Update map layout to focus on India
            fig.update_geos(
                fitbounds="locations",
                visible=False,
                showframe=False,
                showcoastlines=True,
                coastlinecolor="white",
                showland=True,
                landcolor="lightgray",
                showocean=True,
                oceancolor="lightblue"
            )

            fig.update_layout(
                height=600,
                font=dict(size=12),
                title_font_size=16,
                title_x=0.5,
                margin={"r":0,"t":50,"l":0,"b":0},
                coloraxis_colorbar=dict(
                    title="Total Tourists<br>(Million)",
                    title_font_size=12,
                    tickfont_size=10
                )
            )

            st.plotly_chart(fig, use_container_width=True)

            # Map legend as small bold text below the map
            st.markdown("""
            <p style="font-size: 0.85rem; color: #333; text-align: center; margin-top: 0.5rem; font-weight: bold;">
                <strong>Color Intensity:</strong> Total tourist arrivals (2022 + 2023) - Darker shades indicate higher tourist volume |
                <strong>Hover:</strong> Click on states to see detailed tourism statistics and growth rates
            </p>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.warning(f"Choropleth map failed to load, falling back to scatter map. Error: {str(e)}")
            # Fallback to original scatter map if choropleth fails
            create_fallback_scatter_map(map_df)
    else:
        st.warning("Unable to create map - tourism data not available")

def create_fallback_scatter_map(map_df):
    """Fallback scatter map if choropleth fails"""

    # State coordinates for fallback scatter map
    state_coordinates = {
        'Andhra Pradesh': [15.9129, 79.7400],
        'Arunachal Pradesh': [28.2180, 94.7278],
        'Assam': [26.2006, 92.9376],
        'Bihar': [25.0961, 85.3131],
        'Chhattisgarh': [21.2787, 81.8661],
        'Goa': [15.2993, 74.1240],
        'Gujarat': [23.0225, 72.5714],
        'Haryana': [29.0588, 76.0856],
        'Himachal Pradesh': [31.1048, 77.1734],
        'Jharkhand': [23.6102, 85.2799],
        'Karnataka': [15.3173, 75.7139],
        'Kerala': [10.8505, 76.2711],
        'Madhya Pradesh': [22.9734, 78.6569],
        'Maharashtra': [19.7515, 75.7139],
        'Manipur': [24.6637, 93.9063],
        'Meghalaya': [25.4670, 91.3662],
        'Mizoram': [23.1645, 92.9376],
        'Nagaland': [26.1584, 94.5624],
        'Odisha': [20.9517, 85.0985],
        'Punjab': [31.1471, 75.3412],
        'Rajasthan': [27.0238, 74.2179],
        'Sikkim': [27.5330, 88.5122],
        'Tamil Nadu': [11.1271, 78.6569],
        'Telangana': [18.1124, 79.0193],
        'Tripura': [23.9408, 91.9882],
        'Uttar Pradesh': [26.8467, 80.9462],
        'Uttarakhand': [30.0668, 79.0193],
        'West Bengal': [22.9868, 87.8550],
        'Andaman and Nicobar Islands': [11.7401, 92.6586],
        'Chandigarh': [30.7333, 76.7794],
        'Dadra and Nagar Haveli and Daman and Diu': [20.1809, 73.0169],
        'Delhi': [28.7041, 77.1025],
        'Jammu and Kashmir': [34.0837, 74.7973],
        'Ladakh': [34.1526, 77.5771],
        'Lakshadweep': [10.5667, 72.6417],
        'Puducherry': [11.9416, 79.8083]
    }

    # Add coordinates to map data
    for idx, row in map_df.iterrows():
        state_name = row['State']
        if state_name in state_coordinates:
            map_df.at[idx, 'lat'] = state_coordinates[state_name][0]
            map_df.at[idx, 'lon'] = state_coordinates[state_name][1]

    # Filter out states without coordinates
    map_df = map_df.dropna(subset=['lat', 'lon'])

    if not map_df.empty:
        fig = px.scatter_map(
            map_df,
            lat='lat',
            lon='lon',
            size='Total_Tourism_2Years',
            color='Total_Tourism_2Years',
            hover_name='State',
            hover_data={
                'Tourism_2023': ':,.1f',
                'Tourism_2022': ':,.1f',
                'Total_Tourism_2Years': ':,.1f',
                'Growth': ':+.1f%',
                'Region': True,
                'lat': False,
                'lon': False
            },
            color_continuous_scale='Greens',
            size_max=30,
            zoom=4,
            center={'lat': 20.5937, 'lon': 78.9629},
            title='🗺️ India Tourism Map - Total Tourist Arrivals (2022 + 2023)',
            labels={
                'Total_Tourism_2Years': 'Total Tourists (M)'
            }
        )

        fig.update_layout(
            height=600,
            font=dict(size=12),
            title_font_size=16
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <p style="font-size: 0.85rem; color: #333; text-align: center; margin-top: 0.5rem; font-weight: bold;">
            <strong>Circle Size & Color:</strong> Total tourist arrivals (2022 + 2023) - Larger and darker circles indicate higher tourist volume |
            <strong>Hover:</strong> Click on circles to see detailed information
        </p>
        """, unsafe_allow_html=True)

def create_enhanced_tourism_chart(ita_df):
    """Create an enhanced tourism growth chart"""

    # Create subplots with increased spacing
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Tourism Growth Trend', 'Year-over-Year Growth',
                       'Decade Comparison', 'Recovery Analysis'),
        specs=[[{"colspan": 2}, None],
               [{"type": "bar"}, {"type": "bar"}]],
        vertical_spacing=0.25
    )

    # Main trend line - minimalist style
    fig.add_trace(
        go.Scatter(
            x=ita_df['YEAR'],
            y=ita_df['INDIA_ARRIVALS_MILLION'],
            mode='lines+markers',
            name='Tourist Arrivals',
            line=dict(color='#008080', width=2),
            marker=dict(size=6, color='#008080'),
            fill=None
        ),
        row=1, col=1
    )

    # Add COVID impact annotation - minimalist style
    fig.add_annotation(
        x=2020, y=ita_df[ita_df['YEAR'] == 2020]['INDIA_ARRIVALS_MILLION'].iloc[0],
        text="COVID-19",
        showarrow=True,
        arrowhead=1,
        arrowcolor="#666",
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="#ccc",
        borderwidth=1,
        font=dict(size=10, color="#666"),
        row=1, col=1
    )

    # Growth rate chart - minimalist colors
    ita_df_growth = ita_df.copy()
    ita_df_growth['Growth Rate'] = ita_df_growth['INDIA_ARRIVALS_MILLION'].pct_change() * 100

    colors = ['#008080' if x > 0 else '#999' for x in ita_df_growth['Growth Rate'].fillna(0)]

    fig.add_trace(
        go.Bar(
            x=ita_df_growth['YEAR'][1:],
            y=ita_df_growth['Growth Rate'][1:],
            name='Growth Rate',
            marker_color=colors[1:],
            opacity=0.6
        ),
        row=2, col=1
    )

    # Decade comparison - minimalist colors
    decades = {
        '2001-2010': ita_df[(ita_df['YEAR'] >= 2001) & (ita_df['YEAR'] <= 2010)]['INDIA_ARRIVALS_MILLION'].mean(),
        '2011-2020': ita_df[(ita_df['YEAR'] >= 2011) & (ita_df['YEAR'] <= 2020)]['INDIA_ARRIVALS_MILLION'].mean(),
        '2021-2023': ita_df[(ita_df['YEAR'] >= 2021) & (ita_df['YEAR'] <= 2023)]['INDIA_ARRIVALS_MILLION'].mean()
    }

    fig.add_trace(
        go.Bar(
            x=list(decades.keys()),
            y=list(decades.values()),
            name='Decade Average',
            marker_color=['#008080', '#20B2AA', '#66CDAA'],
            opacity=0.6
        ),
        row=2, col=2
    )

    # Add horizontal separator line between top and bottom sections
    fig.add_shape(
        type="line",
        x0=0, x1=1,
        y0=0.50, y1=0.50,
        xref="paper", yref="paper",
        line=dict(color="black", width=3)
    )

    # Update layout - minimalist style
    fig.update_layout(
        height=500,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#666', size=11),
        title_text="",
        margin=dict(l=40, r=40, t=40, b=40)
    )

    # Update axes - minimal grid with black bold labels
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )

    return fig

def create_tourism_growth_trend_chart(ita_df):
    """Create tourism growth trend chart"""

    fig = go.Figure()

    # Main trend line - minimalist style
    fig.add_trace(
        go.Scatter(
            x=ita_df['YEAR'],
            y=ita_df['INDIA_ARRIVALS_MILLION'],
            mode='lines+markers',
            name='Tourist Arrivals',
            line=dict(color='#008080', width=2),
            marker=dict(size=6, color='#008080'),
            fill=None
        )
    )

    # Add COVID impact annotation - minimalist style
    fig.add_annotation(
        x=2020, y=ita_df[ita_df['YEAR'] == 2020]['INDIA_ARRIVALS_MILLION'].iloc[0],
        text="COVID-19",
        showarrow=True,
        arrowhead=1,
        arrowcolor="#666",
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="#ccc",
        borderwidth=1,
        font=dict(size=10, color="#666")
    )

    # Update layout - minimalist style
    fig.update_layout(
        height=300,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='black', size=11),
        title_text="",
        margin=dict(l=40, r=40, t=20, b=40),
        xaxis_title="Year",
        yaxis_title="Tourist Arrivals (Million)"
    )

    # Update axes - minimal grid with black bold labels
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )

    return fig

def create_year_over_year_growth_chart(ita_df):
    """Create year-over-year growth chart"""

    fig = go.Figure()

    # Growth rate chart - minimalist colors
    ita_df_growth = ita_df.copy()
    ita_df_growth['Growth Rate'] = ita_df_growth['INDIA_ARRIVALS_MILLION'].pct_change() * 100

    colors = ['#008080' if x > 0 else '#999' for x in ita_df_growth['Growth Rate'].fillna(0)]

    fig.add_trace(
        go.Bar(
            x=ita_df_growth['YEAR'][1:],
            y=ita_df_growth['Growth Rate'][1:],
            name='Growth Rate',
            marker_color=colors[1:],
            opacity=0.6
        )
    )

    # Update layout - minimalist style
    fig.update_layout(
        height=300,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='black', size=11),
        title_text="",
        margin=dict(l=40, r=40, t=20, b=40),
        xaxis_title="Year",
        yaxis_title="Growth Rate (%)"
    )

    # Update axes - minimal grid with black bold labels
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )

    return fig

def create_decade_comparison_chart(ita_df):
    """Create decade comparison chart"""

    fig = go.Figure()

    # Decade comparison - minimalist colors
    decades = {
        '2001-2010': ita_df[(ita_df['YEAR'] >= 2001) & (ita_df['YEAR'] <= 2010)]['INDIA_ARRIVALS_MILLION'].mean(),
        '2011-2020': ita_df[(ita_df['YEAR'] >= 2011) & (ita_df['YEAR'] <= 2020)]['INDIA_ARRIVALS_MILLION'].mean(),
        '2021-2023': ita_df[(ita_df['YEAR'] >= 2021) & (ita_df['YEAR'] <= 2023)]['INDIA_ARRIVALS_MILLION'].mean()
    }

    fig.add_trace(
        go.Bar(
            x=list(decades.keys()),
            y=list(decades.values()),
            name='Decade Average',
            marker_color=['#008080', '#20B2AA', '#66CDAA'],
            opacity=0.6
        )
    )

    # Update layout - minimalist style
    fig.update_layout(
        height=300,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='black', size=11),
        title_text="",
        margin=dict(l=40, r=40, t=20, b=40),
        xaxis_title="Decade",
        yaxis_title="Average Arrivals (Million)"
    )

    # Update axes - minimal grid with black bold labels
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.3)',
        showline=True,
        linewidth=1,
        linecolor='rgba(200,200,200,0.5)',
        tickfont=dict(color='black', size=11),
        title_font=dict(color='black', size=12)
    )

    return fig

def create_gdp_contribution_chart(tourism_gdp_df):
    """Create GDP contribution chart"""

    fig = go.Figure()

    # Add direct contribution line
    fig.add_trace(
        go.Scatter(
            x=tourism_gdp_df['YEAR'],
            y=tourism_gdp_df['DIRECT_CONTRIBUTION_GDP_PERCENT'],
            mode='lines+markers',
            name='Direct Contribution',
            line=dict(color='#008080', width=3),
            marker=dict(size=8, color='#008080'),
            fill='tonexty',
            fillcolor='rgba(0,128,128,0.1)'
        )
    )

    # Add total contribution line
    fig.add_trace(
        go.Scatter(
            x=tourism_gdp_df['YEAR'],
            y=tourism_gdp_df['TOTAL_CONTRIBUTION_GDP_PERCENT'],
            mode='lines+markers',
            name='Total Contribution (Direct + Indirect)',
            line=dict(color='#20B2AA', width=3),
            marker=dict(size=8, color='#20B2AA'),
            fill='tonexty',
            fillcolor='rgba(32,178,170,0.1)'
        )
    )

    # Add COVID impact annotation
    fig.add_annotation(
        x='2020-21',
        y=tourism_gdp_df[tourism_gdp_df['YEAR'] == '2020-21']['DIRECT_CONTRIBUTION_GDP_PERCENT'].iloc[0],
        text="COVID-19 Impact",
        showarrow=True,
        arrowhead=2,
        arrowcolor="red",
        bgcolor="rgba(255,0,0,0.1)",
        bordercolor="red"
    )

    fig.update_layout(
        title='Tourism Contribution to India\'s GDP',
        xaxis_title='Year',
        yaxis_title='Contribution (%)',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333', size=11),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')

    return fig

def create_employment_trends_chart(tourism_employment_df):
    """Create employment trends chart"""

    fig = go.Figure()

    # Add direct employment
    fig.add_trace(
        go.Scatter(
            x=tourism_employment_df['YEAR'],
            y=tourism_employment_df['TOURISM_CHARACTERISTIC_INDUSTRIES_MILLION'],
            mode='lines+markers',
            name='Direct Tourism Jobs',
            line=dict(color='#FF6B35', width=3),
            marker=dict(size=8, color='#FF6B35'),
            fill='tonexty',
            fillcolor='rgba(255,107,53,0.1)'
        )
    )

    # Add total employment
    fig.add_trace(
        go.Scatter(
            x=tourism_employment_df['YEAR'],
            y=tourism_employment_df['DIRECT_INDIRECT_EMPLOYMENT_MILLION'],
            mode='lines+markers',
            name='Total Tourism Employment',
            line=dict(color='#F18F01', width=3),
            marker=dict(size=8, color='#F18F01'),
            fill='tonexty',
            fillcolor='rgba(241,143,1,0.1)'
        )
    )

    # Add employment share percentage as secondary y-axis
    fig.add_trace(
        go.Scatter(
            x=tourism_employment_df['YEAR'],
            y=tourism_employment_df['DIRECT_INDIRECT_SHARE_PERCENT'],
            mode='lines+markers',
            name='Employment Share (%)',
            line=dict(color='#A23B72', width=2, dash='dash'),
            marker=dict(size=6, color='#A23B72'),
            yaxis='y2'
        )
    )

    fig.update_layout(
        title='Tourism Employment in India',
        xaxis_title='Year',
        yaxis_title='Employment (Million)',
        yaxis2=dict(
            title='Share of Total Employment (%)',
            overlaying='y',
            side='right',
            range=[10, 16]
        ),
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333', size=11),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')

    return fig
