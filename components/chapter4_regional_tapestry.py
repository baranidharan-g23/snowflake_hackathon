import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def show_regional_tapestry(state_total_df, state_domestic_df, state_foreign_df, dance_df, festivals_df):
    """Chapter 4: The Regional Tapestry - State-wise Tourism and Cultural Diversity"""
    
    # Chapter Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FF6347, #FF7F50, #FFA07A); padding: 3rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(255,99,71,0.3);">
        <h1 style="color: white; font-size: 3rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
            🗺️ Chapter 4: The Regional Tapestry
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.3rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
            From Himalayan Heights to Coastal Delights - India's Diverse Tourism Landscape
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Regional Introduction
    st.markdown("""
    <div style="background: rgba(255,99,71,0.05); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; border-left: 6px solid #FF6347;">
        <h3 style="color: #FF6347; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">🌈 India's Cultural Kaleidoscope</h3>
        <p style="color: #555; line-height: 1.8; font-size: 1.1rem; margin: 0;">
            India's tourism isn't just about numbers - it's about the <strong>incredible diversity</strong> across regions. 
            From the <strong>snow-capped Himalayas of the North</strong> to the <strong>tropical backwaters of the South</strong>, 
            from the <strong>desert kingdoms of the West</strong> to the <strong>tribal cultures of the Northeast</strong>, 
            each region offers unique experiences. With <strong>123+ dance forms</strong> and countless festivals, 
            India presents a living museum of human culture and tradition.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Regional Tourism Distribution
    if not state_total_df.empty:
        st.markdown("""
        <div style="background: rgba(255,127,80,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
            <h4 style="color: #FF7F50; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                🎯 Regional Tourism Distribution: Where India Shines
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Calculate regional totals for latest year
        regional_totals = state_total_df.groupby('REGION')['YEAR_2023'].sum().reset_index()
        regional_totals = regional_totals.sort_values('YEAR_2023', ascending=False)

        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Regional distribution chart
            colors = ['#FF6347', '#FF7F50', '#FFA07A', '#FFB6C1', '#FFC0CB']
            
            fig = go.Figure(data=[
                go.Bar(
                    x=regional_totals['REGION'],
                    y=regional_totals['YEAR_2023'],
                    marker_color=colors[:len(regional_totals)],
                    text=[f"{x:.1f}M" for x in regional_totals['YEAR_2023']],
                    textposition='outside',
                    hovertemplate='<b>%{x}</b><br>Visitors: %{y:.1f}M<extra></extra>'
                )
            ])
            
            fig.update_layout(
                title=dict(
                    text="🌟 Regional Tourism Leaders (2023)",
                    font=dict(size=18, color='#FF6347'),
                    x=0.5
                ),
                xaxis_title="Region",
                yaxis_title="Visitors (Millions)",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=500,
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Regional insights
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); margin-bottom: 1rem;">
                <h5 style="color: #FF6347; text-align: center; margin-bottom: 1rem;">🏆 Regional Champions</h5>
            </div>
            """, unsafe_allow_html=True)
            
            for i, (_, row) in enumerate(regional_totals.iterrows()):
                region = row['REGION']
                visitors = row['YEAR_2023']
                percentage = (visitors / regional_totals['YEAR_2023'].sum()) * 100
                
                # Regional descriptions
                descriptions = {
                    'SOUTH': '🌴 Temples & Tech Hubs',
                    'WEST & CENTRAL': '🏖️ Beaches & Business',
                    'NORTH': '🏔️ Heritage & Hills',
                    'EAST': '🎭 Culture & Literature',
                    'NORTH EAST': '🌿 Nature & Tribes'
                }
                
                desc = descriptions.get(region, '🌟 Unique Experiences')
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {colors[i]}, {colors[i]}AA); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; color: white;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-weight: bold; font-size: 0.9rem;">{region}</span>
                        <span style="font-size: 1.1rem;">{visitors:.1f}M</span>
                    </div>
                    <div style="font-size: 0.8rem; margin-top: 0.3rem; opacity: 0.9;">{desc}</div>
                    <div style="background: rgba(255,255,255,0.3); height: 6px; border-radius: 3px; margin-top: 0.5rem;">
                        <div style="background: white; height: 100%; width: {percentage}%; border-radius: 3px;"></div>
                    </div>
                    <small style="opacity: 0.9;">{percentage:.1f}% of total</small>
                </div>
                """, unsafe_allow_html=True)

    # Top Performing States
    if not state_total_df.empty:
        st.markdown("""
        <div style="background: rgba(255,99,71,0.05); padding: 2rem; border-radius: 15px; margin: 3rem 0;">
            <h3 style="color: #FF6347; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                🏆 State Champions: Tourism Powerhouses
            </h3>
        </div>
        """, unsafe_allow_html=True)

        # Top 10 states by total visitors
        top_states = state_total_df.nlargest(10, 'YEAR_2023')

        col1, col2 = st.columns(2)
        
        with col1:
            # Top states chart
            fig = go.Figure(data=[
                go.Bar(
                    y=top_states['STATE'],
                    x=top_states['YEAR_2023'],
                    orientation='h',
                    marker_color='#FF7F50',
                    text=[f"{x:.1f}M" for x in top_states['YEAR_2023']],
                    textposition='outside',
                    hovertemplate='<b>%{y}</b><br>Visitors: %{x:.1f}M<br>Region: %{customdata}<extra></extra>',
                    customdata=top_states['REGION']
                )
            ])
            
            fig.update_layout(
                title=dict(
                    text="🌟 Top 10 States by Visitors (2023)",
                    font=dict(size=16, color='#FF6347'),
                    x=0.5
                ),
                xaxis_title="Visitors (Millions)",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=500,
                margin=dict(l=120)
            )
            
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Growth analysis
            if 'YEAR_2017' in state_total_df.columns:
                # Calculate growth rates
                growth_data = state_total_df.copy()
                growth_data['Growth_Rate'] = ((growth_data['YEAR_2023'] - growth_data['YEAR_2017']) / growth_data['YEAR_2017']) * 100
                growth_data = growth_data.dropna(subset=['Growth_Rate'])
                top_growth = growth_data.nlargest(10, 'Growth_Rate')

                fig = go.Figure(data=[
                    go.Bar(
                        y=top_growth['STATE'],
                        x=top_growth['Growth_Rate'],
                        orientation='h',
                        marker_color='#FFA07A',
                        text=[f"{x:.1f}%" for x in top_growth['Growth_Rate']],
                        textposition='outside',
                        hovertemplate='<b>%{y}</b><br>Growth: %{x:.1f}%<br>Region: %{customdata}<extra></extra>',
                        customdata=top_growth['REGION']
                    )
                ])
                
                fig.update_layout(
                    title=dict(
                        text="🚀 Fastest Growing States (2017-2023)",
                        font=dict(size=16, color='#FFA07A'),
                        x=0.5
                    ),
                    xaxis_title="Growth Rate (%)",
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#333'),
                    height=500,
                    margin=dict(l=120)
                )
                
                st.plotly_chart(fig, use_container_width=True)

    # Cultural Diversity Analysis
    if not dance_df.empty:
        st.markdown("""
        <div style="background: rgba(255,127,80,0.1); padding: 2rem; border-radius: 15px; margin: 3rem 0;">
            <h4 style="color: #FF7F50; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                💃 The Dance of Diversity: 123+ Cultural Forms Across India
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Dance forms by state
        dance_counts = dance_df['STATE'].value_counts().head(10)

        col1, col2 = st.columns(2)
        
        with col1:
            # States with most dance forms
            fig = go.Figure(data=[
                go.Bar(
                    x=dance_counts.index,
                    y=dance_counts.values,
                    marker_color='#FF6347',
                    text=dance_counts.values,
                    textposition='outside',
                    hovertemplate='<b>%{x}</b><br>Dance Forms: %{y}<extra></extra>'
                )
            ])
            
            fig.update_layout(
                title=dict(
                    text="🎭 States with Most Dance Forms",
                    font=dict(size=16, color='#FF6347'),
                    x=0.5
                ),
                xaxis_title="State",
                yaxis_title="Number of Dance Forms",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                xaxis=dict(tickangle=45)
            )
            
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Featured dance forms
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
                <h5 style="color: #FF6347; text-align: center; margin-bottom: 1rem;">🌟 Iconic Dance Forms</h5>
            </div>
            """, unsafe_allow_html=True)
            
            # Highlight some famous dance forms
            famous_dances = [
                ('Bharatanatyam', 'Tamil Nadu', '🎭 Classical Grace'),
                ('Kathak', 'Uttar Pradesh', '💫 Storytelling Spins'),
                ('Bhangra', 'Punjab', '🌾 Harvest Celebration'),
                ('Kuchipudi', 'Andhra Pradesh', '🎪 Dance Drama'),
                ('Garba', 'Gujarat', '🌙 Divine Circles')
            ]
            
            for dance, state, desc in famous_dances:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #FF6347, #FF7F50); padding: 0.8rem; border-radius: 8px; margin: 0.5rem 0; color: white;">
                    <div style="font-weight: bold; font-size: 0.9rem;">{dance}</div>
                    <div style="font-size: 0.8rem; opacity: 0.9;">{state} • {desc}</div>
                </div>
                """, unsafe_allow_html=True)

    # Festival Distribution
    if not festivals_df.empty:
        st.markdown("""
        <div style="background: rgba(255,99,71,0.05); padding: 2rem; border-radius: 15px; margin: 3rem 0;">
            <h3 style="color: #FF6347; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                🎉 Festival Calendar: Celebrations Across Seasons
            </h3>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        
        with col1:
            # Festivals by type
            if 'TYPE' in festivals_df.columns:
                festival_types = festivals_df['TYPE'].value_counts()
                
                fig = go.Figure(data=[go.Pie(
                    labels=festival_types.index,
                    values=festival_types.values,
                    hole=0.4,
                    marker_colors=['#FF6347', '#FF7F50', '#FFA07A'],
                    hovertemplate='<b>%{label}</b><br>Festivals: %{value}<br>Percentage: %{percent}<extra></extra>'
                )])
                
                fig.update_layout(
                    title=dict(
                        text="🎊 Festival Types Distribution",
                        font=dict(size=16, color='#FF6347'),
                        x=0.5
                    ),
                    font=dict(color='#333'),
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Seasonal festival distribution
            if 'MONTH_SEASON' in festivals_df.columns:
                seasonal_festivals = festivals_df['MONTH_SEASON'].value_counts().head(8)
                
                fig = go.Figure(data=[
                    go.Bar(
                        x=seasonal_festivals.index,
                        y=seasonal_festivals.values,
                        marker_color='#FFA07A',
                        text=seasonal_festivals.values,
                        textposition='outside',
                        hovertemplate='<b>%{x}</b><br>Festivals: %{y}<extra></extra>'
                    )
                ])
                
                fig.update_layout(
                    title=dict(
                        text="🌸 Festivals by Season/Month",
                        font=dict(size=16, color='#FFA07A'),
                        x=0.5
                    ),
                    xaxis_title="Season/Month",
                    yaxis_title="Number of Festivals",
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#333'),
                    height=400,
                    xaxis=dict(tickangle=45)
                )
                
                st.plotly_chart(fig, use_container_width=True)

    # Domestic vs Foreign Preferences
    if not state_domestic_df.empty and not state_foreign_df.empty:
        st.markdown("""
        <div style="background: rgba(255,127,80,0.1); padding: 2rem; border-radius: 15px; margin: 3rem 0;">
            <h4 style="color: #FF7F50; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                🇮🇳 vs 🌍 Domestic vs International Preferences
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Top states for domestic vs foreign tourists
        top_domestic = state_domestic_df.nlargest(8, 'YEAR_2023')[['STATE', 'YEAR_2023']]
        top_foreign = state_foreign_df.nlargest(8, 'YEAR_2023')[['STATE', 'YEAR_2023']]

        col1, col2 = st.columns(2)
        
        with col1:
            fig = go.Figure(data=[
                go.Bar(
                    y=top_domestic['STATE'],
                    x=top_domestic['YEAR_2023'],
                    orientation='h',
                    marker_color='#FF6347',
                    text=[f"{x:.1f}M" for x in top_domestic['YEAR_2023']],
                    textposition='outside',
                    hovertemplate='<b>%{y}</b><br>Domestic Visitors: %{x:.1f}M<extra></extra>'
                )
            ])
            
            fig.update_layout(
                title=dict(
                    text="🇮🇳 Top States - Domestic Tourists",
                    font=dict(size=16, color='#FF6347'),
                    x=0.5
                ),
                xaxis_title="Visitors (Millions)",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=450,
                margin=dict(l=100)
            )
            
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig = go.Figure(data=[
                go.Bar(
                    y=top_foreign['STATE'],
                    x=top_foreign['YEAR_2023'],
                    orientation='h',
                    marker_color='#FFA07A',
                    text=[f"{x:.1f}M" for x in top_foreign['YEAR_2023']],
                    textposition='outside',
                    hovertemplate='<b>%{y}</b><br>Foreign Visitors: %{x:.1f}M<extra></extra>'
                )
            ])
            
            fig.update_layout(
                title=dict(
                    text="🌍 Top States - International Tourists",
                    font=dict(size=16, color='#FFA07A'),
                    x=0.5
                ),
                xaxis_title="Visitors (Millions)",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=450,
                margin=dict(l=100)
            )
            
            st.plotly_chart(fig, use_container_width=True)

    # Regional Tapestry Summary
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FF6347, #FF7F50); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
        <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            🌈 India's Regional Tapestry: Unity in Diversity
        </h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #FFD700;">🗺️ Regional Diversity</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">5 distinct tourism regions</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #98FB98;">💃 Cultural Forms</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">123+ dance traditions</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #87CEEB;">🎉 Celebrations</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">Year-round festivals</p>
            </div>
        </div>
        <p style="margin: 2rem 0 0 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
            From the <strong>spiritual Ganges</strong> to the <strong>beaches of Goa</strong>, from <strong>Rajasthani folk dances</strong> 
            to <strong>Bengali literature festivals</strong>, India's regional tapestry offers infinite experiences, 
            making every journey a discovery of new cultures, traditions, and stories.
        </p>
    </div>
    """, unsafe_allow_html=True)
