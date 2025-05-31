import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def show_travelers_journey(ita_df, ita_monthly_df, stay_duration_df, age_statistics_df, all_lean_peak_data):
    """Chapter 3: The Traveler's Journey - Visitor Patterns, Demographics, and Seasonal Trends"""
    
    # Chapter Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4169E1, #6495ED, #87CEEB); padding: 3rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(65,105,225,0.3);">
        <h1 style="color: white; font-size: 3rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
            🌍 Chapter 3: The Traveler's Journey
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.3rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
            22 Years of Global Wanderers - From 2.5M to 18.9M Visitors
        </p>
    </div>
    """, unsafe_allow_html=True)

    # The 22-Year Journey Introduction
    st.markdown("""
    <div style="background: rgba(65,105,225,0.05); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; border-left: 6px solid #4169E1;">
        <h3 style="color: #4169E1; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">🎯 The Great Tourism Transformation (2001-2023)</h3>
        <p style="color: #555; line-height: 1.8; font-size: 1.1rem; margin: 0;">
            From <strong>2.5 million visitors in 2001</strong> to <strong>18.9 million in 2023</strong> - India's tourism story 
            is one of remarkable growth, resilience, and global appeal. This 22-year journey reveals changing visitor demographics, 
            evolving seasonal patterns, and the diverse tapestry of international travelers who choose India as their destination. 
            Each visitor brings their own story, stay duration, and seasonal preferences, creating a rich mosaic of global tourism patterns.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 22-Year Timeline Analysis
    if not ita_df.empty:
        st.markdown("""
        <div style="background: rgba(100,149,237,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
            <h4 style="color: #6495ED; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                📈 The 22-Year Growth Saga: India's Tourism Evolution
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Key milestones
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            start_visitors = ita_df['INDIA_ARRIVALS_MILLION'].iloc[0]
            start_year = ita_df['YEAR'].iloc[0]
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #4169E1, #6495ED); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{start_visitors:.1f}M</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Starting Point</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    {start_year}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            peak_visitors = ita_df['INDIA_ARRIVALS_MILLION'].max()
            peak_year = ita_df.loc[ita_df['INDIA_ARRIVALS_MILLION'].idxmax(), 'YEAR']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #6495ED, #87CEEB); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{peak_visitors:.1f}M</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Historic Peak</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    {peak_year}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            latest_visitors = ita_df['INDIA_ARRIVALS_MILLION'].iloc[-1]
            latest_year = ita_df['YEAR'].iloc[-1]
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #87CEEB, #B0E0E6); padding: 1.5rem; border-radius: 12px; text-align: center; color: #4169E1; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{latest_visitors:.1f}M</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Current Level</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(65,105,225,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    {latest_year}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            growth_multiple = latest_visitors / start_visitors
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #B0E0E6, #F0F8FF); padding: 1.5rem; border-radius: 12px; text-align: center; color: #4169E1; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{growth_multiple:.1f}x</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Growth Multiple</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(65,105,225,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    22 Years
                </p>
            </div>
            """, unsafe_allow_html=True)

        # Main Timeline Chart
        fig = go.Figure()
        
        # Add main trend line
        fig.add_trace(go.Scatter(
            x=ita_df['YEAR'],
            y=ita_df['INDIA_ARRIVALS_MILLION'],
            mode='lines+markers',
            name='Tourist Arrivals',
            line=dict(color='#4169E1', width=4, shape='spline'),
            marker=dict(size=12, color='#4169E1', symbol='circle', line=dict(width=2, color='white')),
            fill='tonexty',
            fillcolor='rgba(65,105,225,0.1)',
            hovertemplate='<b>Year:</b> %{x}<br><b>Arrivals:</b> %{y:.1f}M visitors<extra></extra>'
        ))

        # Highlight COVID period
        fig.add_vrect(
            x0=2019.5, x1=2021.5,
            fillcolor="rgba(255, 99, 71, 0.15)",
            layer="below",
            line_width=0,
            annotation_text="🦠 Pandemic Impact",
            annotation_position="top left"
        )

        # Add recovery annotation
        fig.add_annotation(
            x=2023,
            y=latest_visitors,
            text="🚀 Strong Recovery",
            showarrow=True,
            arrowhead=2,
            arrowcolor="#4169E1",
            bgcolor="rgba(65,105,225,0.1)",
            bordercolor="#4169E1",
            borderwidth=2
        )

        fig.update_layout(
            title=dict(
                text="🌟 India's 22-Year Tourism Journey: From Millions to Global Destination",
                font=dict(size=18, color='#4169E1', family="Georgia"),
                x=0.5
            ),
            xaxis_title="Year",
            yaxis_title="Arrivals (Million)",
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333', size=12),
            height=550,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)

    # Age Demographics Analysis
    if not age_statistics_df.empty:
        st.markdown("""
        <div style="background: rgba(65,105,225,0.05); padding: 2rem; border-radius: 15px; margin: 3rem 0;">
            <h3 style="color: #4169E1; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                👥 The Age of Wanderers: Who Visits India?
            </h3>
            <p style="color: #555; text-align: center; line-height: 1.6; margin: 0;">
                Understanding the demographic profile of India's international visitors
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Latest year age distribution
        latest_age_data = age_statistics_df.iloc[-1]
        age_columns = ['AGE_0_14', 'AGE_15_24', 'AGE_25_34', 'AGE_35_44', 'AGE_45_54', 'AGE_55_64', 'AGE_65_ABOVE FLOAT']
        age_labels = ['0-14', '15-24', '25-34', '35-44', '45-54', '55-64', '65+']
        
        # Clean age data
        age_values = []
        for col in age_columns:
            if col in latest_age_data:
                age_values.append(latest_age_data[col])
            else:
                age_values.append(0)

        col1, col2 = st.columns(2)
        
        with col1:
            # Age Distribution Pie Chart
            fig = go.Figure(data=[go.Pie(
                labels=age_labels,
                values=age_values,
                hole=0.4,
                marker_colors=['#4169E1', '#6495ED', '#87CEEB', '#B0E0E6', '#E6F3FF', '#F0F8FF', '#DCDCDC'],
                hovertemplate='<b>Age Group:</b> %{label}<br><b>Percentage:</b> %{value:.1f}%<extra></extra>'
            )])
            
            fig.update_layout(
                title=dict(
                    text=f"👥 Age Distribution of Visitors ({latest_age_data['YEAR']})",
                    font=dict(size=16, color='#4169E1'),
                    x=0.5
                ),
                font=dict(color='#333'),
                height=400,
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Age trend over time for key groups
            fig = go.Figure()
            
            # Focus on key age groups
            key_groups = ['AGE_25_34', 'AGE_35_44', 'AGE_45_54']
            key_labels = ['25-34 (Prime Travel)', '35-44 (Family Travel)', '45-54 (Mature Travel)']
            colors = ['#4169E1', '#6495ED', '#87CEEB']
            
            for i, (col, label, color) in enumerate(zip(key_groups, key_labels, colors)):
                if col in age_statistics_df.columns:
                    fig.add_trace(go.Scatter(
                        x=age_statistics_df['YEAR'],
                        y=age_statistics_df[col],
                        mode='lines+markers',
                        name=label,
                        line=dict(color=color, width=3),
                        marker=dict(size=8, color=color)
                    ))

            fig.update_layout(
                title=dict(
                    text="📊 Age Group Trends Over Time",
                    font=dict(size=16, color='#4169E1'),
                    x=0.5
                ),
                xaxis_title="Year",
                yaxis_title="Percentage of Visitors",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            
            st.plotly_chart(fig, use_container_width=True)

    # Stay Duration Analysis
    if not stay_duration_df.empty:
        st.markdown("""
        <div style="background: rgba(100,149,237,0.1); padding: 2rem; border-radius: 15px; margin: 3rem 0;">
            <h4 style="color: #6495ED; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                ⏰ How Long Do Visitors Stay? Global Patterns Revealed
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Top 15 countries by latest year stay duration
        latest_stay = stay_duration_df[['COUNTRY_OF_NATIONALITY', 'YEAR_2023']].copy()
        latest_stay = latest_stay.dropna().sort_values('YEAR_2023', ascending=False).head(15)

        col1, col2 = st.columns(2)
        
        with col1:
            # Top countries by stay duration
            fig = go.Figure(data=[
                go.Bar(
                    y=latest_stay['COUNTRY_OF_NATIONALITY'],
                    x=latest_stay['YEAR_2023'],
                    orientation='h',
                    marker_color='#6495ED',
                    text=[f"{x:.1f} days" for x in latest_stay['YEAR_2023']],
                    textposition='outside',
                    hovertemplate='<b>%{y}</b><br>Stay Duration: %{x:.1f} days<extra></extra>'
                )
            ])
            
            fig.update_layout(
                title=dict(
                    text="🌍 Top Countries by Stay Duration (2023)",
                    font=dict(size=16, color='#6495ED'),
                    x=0.5
                ),
                xaxis_title="Stay Duration (Days)",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=500,
                margin=dict(l=120)
            )
            
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Regional stay duration analysis
            regional_mapping = {
                'WESTERN EUROPE': ['United Kingdom', 'Germany', 'France', 'Italy', 'Spain', 'Netherlands'],
                'NORTH AMERICA': ['United States Of America', 'Canada'],
                'SOUTH ASIA': ['Bangladesh', 'Sri Lanka', 'Nepal', 'Pakistan'],
                'EAST ASIA': ['China', 'Japan'],
                'SOUTHEAST ASIA': ['Malaysia', 'Singapore', 'Thailand']
            }
            
            regional_stays = {}
            for region, countries in regional_mapping.items():
                region_data = stay_duration_df[stay_duration_df['COUNTRY_OF_NATIONALITY'].isin(countries)]
                if not region_data.empty:
                    regional_stays[region] = region_data['YEAR_2023'].mean()
            
            if regional_stays:
                regions = list(regional_stays.keys())
                durations = list(regional_stays.values())
                
                fig = go.Figure(data=[
                    go.Bar(
                        x=regions,
                        y=durations,
                        marker_color=['#4169E1', '#6495ED', '#87CEEB', '#B0E0E6', '#E6F3FF'],
                        text=[f"{x:.1f}" for x in durations],
                        textposition='outside',
                        hovertemplate='<b>%{x}</b><br>Avg Stay: %{y:.1f} days<extra></extra>'
                    )
                ])
                
                fig.update_layout(
                    title=dict(
                        text="🗺️ Regional Stay Duration Patterns",
                        font=dict(size=16, color='#6495ED'),
                        x=0.5
                    ),
                    xaxis_title="Region",
                    yaxis_title="Average Stay (Days)",
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#333'),
                    height=500,
                    xaxis=dict(tickangle=45)
                )
                
                st.plotly_chart(fig, use_container_width=True)

    # Seasonal Patterns from Lean/Peak Data
    if all_lean_peak_data and any(not df.empty for df in all_lean_peak_data.values()):
        st.markdown("""
        <div style="background: rgba(65,105,225,0.05); padding: 2rem; border-radius: 15px; margin: 3rem 0;">
            <h3 style="color: #4169E1; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                🌸 Seasonal Preferences: When Different Nations Visit India
            </h3>
            <p style="color: #555; text-align: center; line-height: 1.6; margin: 0;">
                Exploring peak and lean months for different nationalities
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Use latest year data
        latest_lean_peak = all_lean_peak_data.get(2023)
        if latest_lean_peak is not None and not latest_lean_peak.empty:
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Peak months analysis
                peak_months = latest_lean_peak['PEAK_MONTH'].value_counts().head(6)
                
                fig = go.Figure(data=[
                    go.Bar(
                        x=peak_months.index,
                        y=peak_months.values,
                        marker_color='#4169E1',
                        text=peak_months.values,
                        textposition='outside',
                        hovertemplate='<b>%{x}</b><br>Countries: %{y}<extra></extra>'
                    )
                ])
                
                fig.update_layout(
                    title=dict(
                        text="🌟 Most Popular Peak Months",
                        font=dict(size=16, color='#4169E1'),
                        x=0.5
                    ),
                    xaxis_title="Month",
                    yaxis_title="Number of Countries",
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#333'),
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                # Lean months analysis
                lean_months = latest_lean_peak['LEAN_MONTH'].value_counts().head(6)
                
                fig = go.Figure(data=[
                    go.Bar(
                        x=lean_months.index,
                        y=lean_months.values,
                        marker_color='#87CEEB',
                        text=lean_months.values,
                        textposition='outside',
                        hovertemplate='<b>%{x}</b><br>Countries: %{y}<extra></extra>'
                    )
                ])
                
                fig.update_layout(
                    title=dict(
                        text="🌙 Most Common Lean Months",
                        font=dict(size=16, color='#87CEEB'),
                        x=0.5
                    ),
                    xaxis_title="Month",
                    yaxis_title="Number of Countries",
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#333'),
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)

    # Journey Summary
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4169E1, #6495ED); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
        <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            🎯 The Traveler's Journey: Key Insights
        </h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #FFD700;">📈 Growth Story</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">7.6x growth in 22 years</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #98FB98;">👥 Demographics</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">25-44 age group dominates</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #87CEEB;">⏰ Stay Patterns</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">Diverse duration preferences</p>
            </div>
        </div>
        <p style="margin: 2rem 0 0 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
            From young backpackers to mature travelers, from quick business trips to extended cultural journeys, 
            India welcomes a <strong>diverse global community</strong> with varying preferences and patterns.
        </p>
    </div>
    """, unsafe_allow_html=True)
