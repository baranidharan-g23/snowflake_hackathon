import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def show_heritage_heartbeat(unesco_df, top_monuments_domestic_df, top_monuments_foreign_df,
                           centrally_protected_domestic_df, centrally_protected_foreign_df):
    """Chapter 1: The Heritage Heartbeat - UNESCO Sites and Monument Tourism"""

    # Chapter Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #8B4513, #D2691E, #CD853F); padding: 3rem; border-radius: 25px; margin: 2rem 0; text-align: center; box-shadow: 0 15px 35px rgba(139,69,19,0.3);">
        <h1 style="color: white; font-size: 3rem; margin-bottom: 1rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); font-family: 'Georgia', serif;">
            🏛️ Chapter 1: The Heritage Heartbeat
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.3rem; margin: 0; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">
            Where Ancient Stones Tell Timeless Stories - India's UNESCO Legacy & Monument Magnificence
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Story Introduction
    st.markdown("""
    <div style="background: rgba(139,69,19,0.05); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; border-left: 6px solid #8B4513;">
        <h3 style="color: #8B4513; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">📜 The Living Chronicle of India's Heritage</h3>
        <p style="color: #555; line-height: 1.8; font-size: 1.1rem; margin: 0;">
            From the <strong>majestic Ajanta Caves (1983)</strong> to the recent <strong>Moidams of Assam (2024)</strong>,
            India's 43 UNESCO World Heritage Sites represent over <strong>4 decades of global recognition</strong>.
            Each monument tells a story spanning millennia - from ancient Buddhist art to Mughal grandeur,
            from colonial architecture to tribal burial traditions. These aren't just tourist destinations;
            they are <strong>living testimonies</strong> of human civilization, creativity, and cultural continuity.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Top 5 UNESCO Sites by Visits
    if not top_monuments_domestic_df.empty:
        st.markdown("""
        <div style="background: rgba(210,105,30,0.1); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
            <h4 style="color: #D2691E; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
                🏆 Top 5 UNESCO Heritage Sites: Where Millions Come to Marvel
            </h4>
        </div>
        """, unsafe_allow_html=True)

        # Create mapping of monument names to UNESCO data
        monument_to_unesco = {
            'Taj Mahal': 'Taj Mahal',
            'Red Fort': 'Red Fort Complex',
            'Qutub Minar': 'Qutb Minar and its Monuments, Delhi',
            'Agra Fort': 'Agra Fort',
            'Sun Temple Konark': 'Sun Temple, Odisha',
            'Group of Monuments Mamallapuram': 'Group of Monuments at Mahabalipuram',
            'Ellora Caves': 'Ellora Caves'
        }

        # Get UNESCO sites that appear in top monuments
        unesco_sites_data = []
        for _, monument_row in top_monuments_domestic_df.iterrows():
            monument_name = monument_row['MONUMENT_NAME']
            if monument_name in monument_to_unesco:
                unesco_name = monument_to_unesco[monument_name]
                # Find UNESCO data
                unesco_match = unesco_df[unesco_df['Site'] == unesco_name]
                if not unesco_match.empty:
                    unesco_info = unesco_match.iloc[0]
                    unesco_sites_data.append({
                        'monument_name': monument_name,
                        'unesco_name': unesco_name,
                        'visits': monument_row['DOMESTIC_TOTAL_VISITS_MILLIONS'],
                        'share': monument_row['PERCENTAGE_SHARE'],
                        'year': unesco_info['Year'],
                        'description': unesco_info['Description'][:100] + "..." if len(unesco_info['Description']) > 100 else unesco_info['Description'],
                        'image': unesco_info['Image_Name'],
                        'location': unesco_info['Location']
                    })

        # Sort by visits and take top 5
        unesco_sites_data = sorted(unesco_sites_data, key=lambda x: x['visits'], reverse=True)[:5]

        if unesco_sites_data:
            # Create podium-style display
            st.markdown("""
            <div style="text-align: center; margin: 2rem 0;">
                <h5 style="color: #8B4513; margin-bottom: 2rem;">🥇 The UNESCO Champions League</h5>
            </div>
            """, unsafe_allow_html=True)

            # Top 3 podium
            if len(unesco_sites_data) >= 3:
                col1, col2, col3 = st.columns([1, 1.2, 1])

                # 2nd Place
                with col1:
                    site = unesco_sites_data[1]

                    # Display image if available
                    try:
                        st.image(f"Images/unesco_india_images/{site['image']}", width=250, caption=f"🥈 Runner-up: {site['unesco_name']}")
                    except:
                        st.markdown(f"""
                        <div style="background: #f0f0f0; padding: 1.5rem; border-radius: 10px; text-align: center; margin-bottom: 1rem;">
                            <div style="font-size: 3rem; color: #ccc;">🏛️</div>
                            <small style="color: #666;">Image not available</small>
                        </div>
                        """, unsafe_allow_html=True)

                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #C0C0C0, #E5E5E5); padding: 1.5rem 1rem; border-radius: 15px; text-align: center; color: #333;">
                        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🥈</div>
                        <h6 style="margin: 0.5rem 0; font-weight: bold; color: #666;">{site['unesco_name']}</h6>
                        <div style="font-size: 1.5rem; font-weight: bold; color: #8B4513; margin: 0.5rem 0;">{site['visits']:.1f}M</div>
                        <small style="color: #666;">Domestic Visitors</small>
                        <div style="margin-top: 1rem; padding: 0.5rem; background: rgba(139,69,19,0.1); border-radius: 8px;">
                            <small style="color: #8B4513; font-weight: bold;">UNESCO {site['year']} • {site['location']}</small>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                # 1st Place (Champion)
                with col2:
                    site = unesco_sites_data[0]

                    # Display image if available
                    try:
                        st.image(f"Images/unesco_india_images/{site['image']}", width=300, caption=f"🏆 Champion: {site['unesco_name']}")
                    except:
                        st.markdown(f"""
                        <div style="background: #f0f0f0; padding: 2rem; border-radius: 10px; text-align: center; margin-bottom: 1rem;">
                            <div style="font-size: 4rem; color: #ccc;">🏛️</div>
                            <small style="color: #666;">Image not available</small>
                        </div>
                        """, unsafe_allow_html=True)

                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #FFD700, #FFA500); padding: 2rem 1rem; border-radius: 15px; text-align: center; color: white; box-shadow: 0 10px 25px rgba(255,215,0,0.3);">
                        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🏆</div>
                        <h5 style="margin: 0.5rem 0; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">{site['unesco_name']}</h5>
                        <div style="font-size: 2rem; font-weight: bold; margin: 0.5rem 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">{site['visits']:.1f}M</div>
                        <small style="opacity: 0.9;">Domestic Visitors</small>
                        <div style="margin-top: 1rem; padding: 0.5rem; background: rgba(255,255,255,0.2); border-radius: 8px;">
                            <small style="font-weight: bold;">UNESCO {site['year']} • {site['location']} • {site['share']:.1f}% Share</small>
                        </div>
                        <div style="margin-top: 0.5rem; font-size: 0.85rem; opacity: 0.9; font-style: italic; line-height: 1.3;">
                            {site['description']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                # 3rd Place
                with col3:
                    site = unesco_sites_data[2]

                    # Display image if available
                    try:
                        st.image(f"Images/unesco_india_images/{site['image']}", width=250, caption=f"🥉 Third place: {site['unesco_name']}")
                    except:
                        st.markdown(f"""
                        <div style="background: #f0f0f0; padding: 1.5rem; border-radius: 10px; text-align: center; margin-bottom: 1rem;">
                            <div style="font-size: 3rem; color: #ccc;">🏛️</div>
                            <small style="color: #666;">Image not available</small>
                        </div>
                        """, unsafe_allow_html=True)

                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #CD7F32, #D2691E); padding: 1.5rem 1rem; border-radius: 15px; text-align: center; color: white;">
                        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🥉</div>
                        <h6 style="margin: 0.5rem 0; font-weight: bold;">{site['unesco_name']}</h6>
                        <div style="font-size: 1.5rem; font-weight: bold; margin: 0.5rem 0;">{site['visits']:.1f}M</div>
                        <small style="opacity: 0.9;">Domestic Visitors</small>
                        <div style="margin-top: 1rem; padding: 0.5rem; background: rgba(255,255,255,0.2); border-radius: 8px;">
                            <small style="font-weight: bold;">UNESCO {site['year']} • {site['location']}</small>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            # 4th and 5th place
            if len(unesco_sites_data) >= 5:
                st.markdown("<br>", unsafe_allow_html=True)
                col1, col2 = st.columns(2)

                with col1:
                    site = unesco_sites_data[3]
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #8B4513, #D2691E); padding: 1.5rem; border-radius: 12px; color: white;">
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <div style="font-size: 2rem;">4️⃣</div>
                            <div style="flex: 1;">
                                <h6 style="margin: 0; font-weight: bold;">{site['unesco_name']}</h6>
                                <div style="font-size: 1.2rem; font-weight: bold;">{site['visits']:.1f}M visitors</div>
                                <small style="opacity: 0.9;">UNESCO {site['year']} • {site['location']}</small>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    site = unesco_sites_data[4]
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #8B4513, #D2691E); padding: 1.5rem; border-radius: 12px; color: white;">
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <div style="font-size: 2rem;">5️⃣</div>
                            <div style="flex: 1;">
                                <h6 style="margin: 0; font-weight: bold;">{site['unesco_name']}</h6>
                                <div style="font-size: 1.2rem; font-weight: bold;">{site['visits']:.1f}M visitors</div>
                                <small style="opacity: 0.9;">UNESCO {site['year']} • {site['location']}</small>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        # UNESCO vs Non-UNESCO comparison
        st.markdown("""
        <div style="background: rgba(255,248,220,0.8); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #FFD700;">
            <h5 style="color: #B8860B; margin-bottom: 1rem;">💡 UNESCO Magic: The Global Recognition Effect</h5>
            <p style="color: #666; line-height: 1.6; margin: 0;">
                UNESCO World Heritage status acts as a <strong>global quality seal</strong>, attracting millions of visitors who seek
                authentic cultural experiences. These sites represent <strong>outstanding universal value</strong> and are protected
                for future generations, making them must-visit destinations for cultural tourism.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # UNESCO Insights Section
    if not unesco_df.empty:
        st.markdown("""
        <div style="background: rgba(255,248,220,0.8); padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #FFD700;">
            <h4 style="color: #B8860B; margin-bottom: 1rem;">💡 UNESCO Heritage Insights</h4>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            total_sites = len(unesco_df)
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h3 style="color: #8B4513; margin: 0; font-size: 2.5rem;">{total_sites}</h3>
                <p style="color: #666; margin: 0.5rem 0 0 0;">UNESCO Sites</p>
                <small style="color: #999;">Global Recognition</small>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            years_span = unesco_df['Year'].max() - unesco_df['Year'].min() + 1 if not unesco_df.empty else 0
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h3 style="color: #D2691E; margin: 0; font-size: 2.5rem;">{years_span}</h3>
                <p style="color: #666; margin: 0.5rem 0 0 0;">Years Journey</p>
                <small style="color: #999;">1983-2024</small>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            # Count unique states
            unique_states = len(unesco_df['Location'].str.split().str[-1].unique()) if not unesco_df.empty else 0
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h3 style="color: #CD853F; margin: 0; font-size: 2.5rem;">{unique_states}</h3>
                <p style="color: #666; margin: 0.5rem 0 0 0;">States/UTs</p>
                <small style="color: #999;">Pan-India Heritage</small>
            </div>
            """, unsafe_allow_html=True)

    # Monument Visitor Analysis
    st.markdown("""
    <div style="background: rgba(139,69,19,0.05); padding: 2rem; border-radius: 15px; margin: 3rem 0;">
        <h3 style="color: #8B4513; text-align: center; margin-bottom: 1.5rem; font-family: 'Georgia', serif;">
            🎯 Monument Magnetism: Where Millions Come to Marvel
        </h3>
        <p style="color: #555; text-align: center; line-height: 1.6; margin: 0;">
            Discover which monuments capture the hearts of domestic and international visitors
        </p>
    </div>
    """, unsafe_allow_html=True)

    if not top_monuments_domestic_df.empty and not top_monuments_foreign_df.empty:
        col1, col2 = st.columns(2)

        with col1:
            # Domestic Visitors Chart
            fig_domestic = go.Figure(data=[
                go.Bar(
                    y=top_monuments_domestic_df['MONUMENT_NAME'][:10],
                    x=top_monuments_domestic_df['DOMESTIC_TOTAL_VISITS_MILLIONS'][:10],
                    orientation='h',
                    marker_color='#8B4513',
                    text=[f"{x:.1f}M" for x in top_monuments_domestic_df['DOMESTIC_TOTAL_VISITS_MILLIONS'][:10]],
                    textposition='outside',
                    hovertemplate='<b>%{y}</b><br>Visitors: %{x:.1f}M<br>Share: %{customdata:.1f}%<extra></extra>',
                    customdata=top_monuments_domestic_df['PERCENTAGE_SHARE'][:10]
                )
            ])

            fig_domestic.update_layout(
                title=dict(
                    text="🇮🇳 Domestic Visitors' Top Choices",
                    font=dict(size=16, color='#8B4513'),
                    x=0.5
                ),
                xaxis_title="Visitors (Millions)",
                plot_bgcolor='rgba(248,249,250,0.8)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=500,
                margin=dict(l=150)
            )

            st.plotly_chart(fig_domestic, use_container_width=True)

        with col2:
            # Foreign Visitors Chart (if available)
            if 'FOREIGN_TOTAL_VISITS_THOUSANDS' in top_monuments_foreign_df.columns:
                fig_foreign = go.Figure(data=[
                    go.Bar(
                        y=top_monuments_foreign_df['MONUMENT_NAME'][:10],
                        x=top_monuments_foreign_df['FOREIGN_TOTAL_VISITS_THOUSANDS'][:10],
                        orientation='h',
                        marker_color='#D2691E',
                        text=[f"{x:.0f}K" for x in top_monuments_foreign_df['FOREIGN_TOTAL_VISITS_THOUSANDS'][:10]],
                        textposition='outside',
                        hovertemplate='<b>%{y}</b><br>Visitors: %{x:.0f}K<extra></extra>'
                    )
                ])

                fig_foreign.update_layout(
                    title=dict(
                        text="🌍 International Visitors' Favorites",
                        font=dict(size=16, color='#D2691E'),
                        x=0.5
                    ),
                    xaxis_title="Visitors (Thousands)",
                    plot_bgcolor='rgba(248,249,250,0.8)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#333'),
                    height=500,
                    margin=dict(l=150)
                )

                st.plotly_chart(fig_foreign, use_container_width=True)

    # Heritage Impact Story
    st.markdown("""
    <div style="background: linear-gradient(135deg, #8B4513, #D2691E); padding: 2.5rem; border-radius: 20px; margin: 3rem 0; color: white; text-align: center;">
        <h3 style="margin-bottom: 1.5rem; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            🌟 The Heritage Impact: Beyond Tourism
        </h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #FFD700;">🏛️ Cultural Preservation</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">Safeguarding 5000+ years of heritage</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #98FB98;">💼 Employment</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">Millions of livelihoods supported</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h4 style="margin: 0 0 0.5rem 0; color: #87CEEB;">🎓 Education</h4>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">Living classrooms of history</p>
            </div>
        </div>
        <p style="margin: 2rem 0 0 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.9;">
            India's heritage sites are not just monuments; they are <strong>economic engines</strong>,
            <strong>cultural ambassadors</strong>, and <strong>bridges between past and future</strong>,
            contributing billions to the economy while preserving invaluable human legacy.
        </p>
    </div>
    """, unsafe_allow_html=True)
