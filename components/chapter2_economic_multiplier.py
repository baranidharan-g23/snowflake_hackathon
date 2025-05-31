import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def show_economic_multiplier(tourism_gdp_df, tourism_employment_df, fee_earnings_df, india_world_share_df):
    """Chapter 2: The Economic Multiplier Story - Tourism's Economic Impact"""

    # Chapter Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2E8B57, #3CB371, #90EE90); padding: 3rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(46,139,87,0.3);">
        <h1 style="color: white; font-size: 3rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
            💰 Chapter 2: The Economic Multiplier Story
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.3rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
            How Every ₹1 in Tourism Becomes ₹1.92 - The Magic of Economic Multiplication
        </p>
    </div>
    """, unsafe_allow_html=True)

    # The Multiplier Story Introduction
    st.markdown("""
    <div style="background: rgba(46,139,87,0.05); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; border-left: 6px solid #2E8B57;">
        <h3 style="color: #2E8B57; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">🎯 The ₹1 → ₹1.92 Magic Formula</h3>
        <p style="color: #555; line-height: 1.8; font-size: 1.1rem; margin: 0;">
            Tourism isn't just about visitors and monuments - it's about <strong>economic multiplication</strong>.
            When a tourist spends ₹1 directly on tourism, it generates an additional ₹0.92 through indirect and induced effects,
            creating a <strong>total economic impact of ₹1.92</strong>. This multiplier effect ripples through hotels, restaurants,
            transportation, handicrafts, and countless other sectors, making tourism one of India's most powerful economic engines.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # GDP Contribution Analysis
    if not tourism_gdp_df.empty:
        st.markdown("""
        <div style="background: rgba(60,179,113,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
            <h4 style="color: #3CB371; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                📈 Tourism's GDP Contribution: The Growth Engine
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Key metrics from latest year
        latest_year = tourism_gdp_df['YEAR'].iloc[-1]
        latest_data = tourism_gdp_df.iloc[-1]

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            direct_gdp = latest_data['DIRECT_CONTRIBUTION_GDP_PERCENT']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #2E8B57, #3CB371); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{direct_gdp:.1f}%</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Direct GDP Share</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    {latest_year}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            total_gdp = latest_data['TOTAL_CONTRIBUTION_GDP_PERCENT']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #3CB371, #90EE90); padding: 1.5rem; border-radius: 12px; text-align: center; color: white; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{total_gdp:.1f}%</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Total GDP Impact</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    With Multiplier
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            multiplier = latest_data['GVA_MULTIPLIER']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #90EE90, #98FB98); padding: 1.5rem; border-radius: 12px; text-align: center; color: #2E8B57; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 2rem;">{multiplier:.2f}x</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Economic Multiplier</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(46,139,87,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    Magic Formula
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            tourism_gdp_crore = latest_data['TOURISM_DIRECT_GDP_CRORE']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #98FB98, #F0FFF0); padding: 1.5rem; border-radius: 12px; text-align: center; color: #2E8B57; margin-bottom: 1rem;">
                <h3 style="margin: 0; font-size: 1.5rem;">₹{tourism_gdp_crore:,.0f}</h3>
                <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.9;">Crores Direct GDP</p>
                <p style="margin: 0; font-size: 0.8rem; background: rgba(46,139,87,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; display: inline-block;">
                    {latest_year}
                </p>
            </div>
            """, unsafe_allow_html=True)

        # GDP Trend Analysis
        col1, col2 = st.columns(2)

        with col1:
            # Direct vs Total GDP Contribution
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=tourism_gdp_df['YEAR'],
                y=tourism_gdp_df['DIRECT_CONTRIBUTION_GDP_PERCENT'],
                mode='lines+markers',
                name='Direct Contribution',
                line=dict(color='#2E8B57', width=4),
                marker=dict(size=10, color='#2E8B57'),
                hovertemplate='<b>Direct GDP:</b> %{y:.2f}%<br><b>Year:</b> %{x}<extra></extra>'
            ))

            fig.add_trace(go.Scatter(
                x=tourism_gdp_df['YEAR'],
                y=tourism_gdp_df['TOTAL_CONTRIBUTION_GDP_PERCENT'],
                mode='lines+markers',
                name='Total Impact (with Multiplier)',
                line=dict(color='#90EE90', width=4),
                marker=dict(size=10, color='#90EE90'),
                hovertemplate='<b>Total GDP:</b> %{y:.2f}%<br><b>Year:</b> %{x}<extra></extra>'
            ))

            fig.update_layout(
                title=dict(
                    text="📊 Tourism's GDP Contribution: Direct vs Total Impact",
                    font=dict(size=16, color='#2E8B57'),
                    x=0.5
                ),
                xaxis_title="Year",
                yaxis_title="GDP Contribution (%)",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # GDP Value in Crores
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=tourism_gdp_df['YEAR'],
                y=tourism_gdp_df['TOURISM_DIRECT_GDP_CRORE'],
                name='Direct GDP (₹ Crores)',
                marker_color='#3CB371',
                text=[f"₹{x:,.0f}" for x in tourism_gdp_df['TOURISM_DIRECT_GDP_CRORE']],
                textposition='outside',
                hovertemplate='<b>Direct GDP:</b> ₹%{y:,.0f} crores<br><b>Year:</b> %{x}<extra></extra>'
            ))

            fig.update_layout(
                title=dict(
                    text="💰 Tourism's Direct GDP Value (₹ Crores)",
                    font=dict(size=16, color='#2E8B57'),
                    x=0.5
                ),
                xaxis_title="Year",
                yaxis_title="GDP Value (₹ Crores)",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                showlegend=False
            )

            st.plotly_chart(fig, use_container_width=True)

    # Employment Impact
    if not tourism_employment_df.empty:
        st.markdown("""
        <div style="background: rgba(46,139,87,0.05); padding: 2rem; border-radius: 15px; margin: 3rem 0;">
            <h3 style="color: #2E8B57; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                👥 Employment Engine: Millions of Livelihoods
            </h3>
            <p style="color: #555; text-align: center; line-height: 1.6; margin: 0;">
                Tourism doesn't just generate revenue - it creates jobs across the entire economy
            </p>
        </div>
        """, unsafe_allow_html=True)

        latest_emp_data = tourism_employment_df.iloc[-1]

        col1, col2, col3 = st.columns(3)

        with col1:
            direct_emp = latest_emp_data['TOURISM_CHARACTERISTIC_INDUSTRIES_MILLION']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #2E8B57, #3CB371); padding: 2rem; border-radius: 15px; text-align: center; color: white;">
                <h3 style="margin: 0; font-size: 2.5rem;">{direct_emp:.1f}M</h3>
                <p style="margin: 0.5rem 0; font-size: 1rem; opacity: 0.9;">Direct Employment</p>
                <small style="opacity: 0.8;">Tourism Industries</small>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            total_emp = latest_emp_data['DIRECT_INDIRECT_EMPLOYMENT_MILLION']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #3CB371, #90EE90); padding: 2rem; border-radius: 15px; text-align: center; color: white;">
                <h3 style="margin: 0; font-size: 2.5rem;">{total_emp:.1f}M</h3>
                <p style="margin: 0.5rem 0; font-size: 1rem; opacity: 0.9;">Total Employment</p>
                <small style="opacity: 0.8;">Direct + Indirect</small>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            emp_share = latest_emp_data['DIRECT_INDIRECT_SHARE_PERCENT']
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #90EE90, #98FB98); padding: 2rem; border-radius: 15px; text-align: center; color: #2E8B57;">
                <h3 style="margin: 0; font-size: 2.5rem;">{emp_share:.1f}%</h3>
                <p style="margin: 0.5rem 0; font-size: 1rem; opacity: 0.9;">of Total Employment</p>
                <small style="opacity: 0.8;">National Share</small>
            </div>
            """, unsafe_allow_html=True)

        # Employment Trend
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=tourism_employment_df['YEAR'],
            y=tourism_employment_df['TOURISM_CHARACTERISTIC_INDUSTRIES_MILLION'],
            mode='lines+markers',
            name='Direct Employment',
            line=dict(color='#2E8B57', width=4),
            marker=dict(size=12, color='#2E8B57'),
            fill='tonexty',
            fillcolor='rgba(46,139,87,0.1)'
        ))

        fig.add_trace(go.Scatter(
            x=tourism_employment_df['YEAR'],
            y=tourism_employment_df['DIRECT_INDIRECT_EMPLOYMENT_MILLION'],
            mode='lines+markers',
            name='Total Employment (Direct + Indirect)',
            line=dict(color='#90EE90', width=4),
            marker=dict(size=12, color='#90EE90')
        ))

        fig.update_layout(
            title=dict(
                text="👥 Tourism Employment Growth: Creating Millions of Jobs",
                font=dict(size=18, color='#2E8B57'),
                x=0.5
            ),
            xaxis_title="Year",
            yaxis_title="Employment (Millions)",
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333'),
            height=500,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

        st.plotly_chart(fig, use_container_width=True)

    # Revenue and Global Position
    if not fee_earnings_df.empty and not india_world_share_df.empty:
        st.markdown("""
        <div style="background: rgba(60,179,113,0.1); padding: 2rem; border-radius: 15px; margin: 3rem 0;">
            <h4 style="color: #3CB371; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                🌍 Global Tourism Revenue & India's Rising Rank
            </h4>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            # Revenue Growth
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=fee_earnings_df['YEAR'],
                y=fee_earnings_df['FEE_CRORE'],
                mode='lines+markers',
                name='Revenue (₹ Crores)',
                line=dict(color='#2E8B57', width=4),
                marker=dict(size=10, color='#2E8B57'),
                hovertemplate='<b>Revenue:</b> ₹%{y:,.0f} crores<br><b>Year:</b> %{x}<extra></extra>'
            ))

            fig.update_layout(
                title=dict(
                    text="💰 Tourism Revenue Growth (₹ Crores)",
                    font=dict(size=16, color='#2E8B57'),
                    x=0.5
                ),
                xaxis_title="Year",
                yaxis_title="Revenue (₹ Crores)",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                showlegend=False
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Global Ranking
            fig = go.Figure()

            # Convert rank to numeric (remove 'th', 'st', 'nd', 'rd')
            ranks = india_world_share_df['INDIA_WORLD_RANK'].str.extract(r'(\d+)')[0].astype(int)

            fig.add_trace(go.Scatter(
                x=india_world_share_df['YEAR'],
                y=ranks,
                mode='lines+markers',
                name='Global Rank',
                line=dict(color='#3CB371', width=4),
                marker=dict(size=10, color='#3CB371'),
                hovertemplate='<b>Rank:</b> %{y}<br><b>Year:</b> %{x}<br><b>Share:</b> %{customdata:.2f}%<extra></extra>',
                customdata=india_world_share_df['INDIA_WORLD_SHARE_PERCENT']
            ))

            fig.update_layout(
                title=dict(
                    text="🏆 India's Global Tourism Ranking",
                    font=dict(size=16, color='#3CB371'),
                    x=0.5
                ),
                xaxis_title="Year",
                yaxis_title="Global Rank",
                yaxis=dict(autorange="reversed"),  # Lower rank number is better
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=400,
                showlegend=False
            )

            st.plotly_chart(fig, use_container_width=True)

    # Economic Impact Summary
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2E8B57, #3CB371); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
        <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            🎯 The Economic Multiplier in Action
        </h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #FFD700;">💰 Revenue Impact</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">₹2.3+ Lakh Crores (2023)</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #98FB98;">👥 Employment</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">76+ Million Jobs</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #87CEEB;">🌍 Global Rank</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">13th Position Worldwide</p>
            </div>
        </div>
        <p style="margin: 2rem 0 0 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
            The <strong>₹1 → ₹1.92 multiplier effect</strong> demonstrates tourism's power as an economic catalyst,
            creating ripple effects across industries and transforming India into a global tourism powerhouse.
        </p>
    </div>
    """, unsafe_allow_html=True)
