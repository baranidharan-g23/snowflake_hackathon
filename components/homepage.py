import streamlit as st
import pandas as pd
import os
from PIL import Image
from utils.helpers import create_india_map, create_tourism_growth_trend_chart, create_year_over_year_growth_chart, create_decade_comparison_chart, create_gdp_contribution_chart, create_employment_trends_chart

def show_homepage(festivals_df, ita_df, state_tourism_df, tourism_gdp_df=None, tourism_employment_df=None):
    """Display enhanced homepage with overview including GDP and employment stats"""

    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">🇮🇳 भारत की सांस्कृतिक विरासत</h1>
        <h1 class="hero-title">Indian Cultural Heritage & Tourism</h1>
        <p class="hero-subtitle">Discover India's Rich Cultural Tapestry Through Data-Driven Insights</p>
        <p class="hero-subtitle">🌟 Preserving Traditions • Exploring Heritage • Celebrating Diversity 🌟</p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced Key Metrics with better styling - Economic Impact
    st.markdown('<div class="stats-grid">', unsafe_allow_html=True)

    # Economic Impact metrics
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        # Tourism GDP contribution
        if tourism_gdp_df is not None and not tourism_gdp_df.empty:
            latest_gdp_contribution = tourism_gdp_df['DIRECT_CONTRIBUTION_GDP_PERCENT'].iloc[-1]
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">💰</div>
                <div class="metric-number">{latest_gdp_contribution:.1f}%</div>
                <div class="metric-label">GDP Contribution</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-icon">💰</div>
                <div class="metric-number">2.6%</div>
                <div class="metric-label">GDP Contribution</div>
            </div>
            """, unsafe_allow_html=True)

    with col6:
        # Tourism employment
        if tourism_employment_df is not None and not tourism_employment_df.empty:
            latest_employment = tourism_employment_df['TOURISM_CHARACTERISTIC_INDUSTRIES_MILLION'].iloc[-1]
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">👥</div>
                <div class="metric-number">{latest_employment:.1f}M</div>
                <div class="metric-label">Tourism Jobs</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-icon">👥</div>
                <div class="metric-number">33M</div>
                <div class="metric-label">Tourism Jobs</div>
            </div>
            """, unsafe_allow_html=True)

    with col7:
        # Total tourism employment (direct + indirect)
        if tourism_employment_df is not None and not tourism_employment_df.empty:
            total_employment = tourism_employment_df['DIRECT_INDIRECT_EMPLOYMENT_MILLION'].iloc[-1]
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">🏢</div>
                <div class="metric-number">{total_employment:.1f}M</div>
                <div class="metric-label">Total Tourism Employment</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-icon">🏢</div>
                <div class="metric-number">76M</div>
                <div class="metric-label">Total Tourism Employment</div>
            </div>
            """, unsafe_allow_html=True)

    with col8:
        # Tourism's share in total employment
        if tourism_employment_df is not None and not tourism_employment_df.empty:
            employment_share = tourism_employment_df['DIRECT_INDIRECT_SHARE_PERCENT'].iloc[-1]
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">📊</div>
                <div class="metric-number">{employment_share:.1f}%</div>
                <div class="metric-label">Employment Share</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-icon">📊</div>
                <div class="metric-number">12.6%</div>
                <div class="metric-label">Employment Share</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Call to Action - moved above Explore India
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 15px; margin: 3rem 0; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <h2 style="color: #008080; margin-bottom: 1rem;">🚀 Start Your Cultural Journey</h2>
        <p style="color: #333; font-size: 1.1rem;">
            Use the navigation menu to explore different sections and discover India's incredible cultural diversity!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Tourism Trends Visualization - moved below Start Cultural Journey
    if not ita_df.empty:
        # 1. Tourism Growth Trend
        st.markdown('<h3 style="color: white; text-align: center; margin-bottom: 1rem;">📊 Tourism Growth Trend</h3>', unsafe_allow_html=True)
        fig_trend = create_tourism_growth_trend_chart(ita_df)
        st.plotly_chart(fig_trend, use_container_width=True)

        # 2. Year-over-Year Growth and Decade Comparison side by side
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<h3 style="color: white; text-align: center; margin-bottom: 1rem;">📈 Year-over-Year Growth</h3>', unsafe_allow_html=True)
            fig_growth = create_year_over_year_growth_chart(ita_df)
            st.plotly_chart(fig_growth, use_container_width=True)

        with col2:
            st.markdown('<h3 style="color: white; text-align: center; margin-bottom: 1rem;">📊 Decade Comparison</h3>', unsafe_allow_html=True)
            fig_decade = create_decade_comparison_chart(ita_df)
            st.plotly_chart(fig_decade, use_container_width=True)

    # Interactive India Map Section
    st.markdown('<h2 class="section-header">🗺️ Explore India</h2>', unsafe_allow_html=True)

    # Create an interactive map of India with state-wise tourism data
    if not state_tourism_df.empty:
        create_india_map(state_tourism_df)

    # Display cultural highlights in an attractive grid
    show_cultural_highlights(festivals_df)



    # Simple Footer
    st.markdown("""
    <div style="margin-top: 4rem; padding: 2rem; background-color: #f8f9fa; border-radius: 10px; text-align: center;">
        <p style="color: #008080; margin-bottom: 0.5rem; font-size: 1.2rem; font-weight: bold;">🇮🇳 Indian Cultural Heritage & Tourism Dashboard</p>
        <p style="color: #20B2AA; font-size: 1.1rem; margin-bottom: 0;">
            Preserving India's Rich Cultural Legacy Through Data-Driven Insights |
            Built with ❤️ for Cultural Heritage Preservation
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_cultural_highlights(festivals_df):
    """Display enhanced cultural highlights with modern card design and animations"""

    if festivals_df.empty:
        st.info("Cultural highlights will be displayed when festival data is available")
        return

    # Enhanced Cultural Highlights with tabs for different categories

    # Create tabs for different cultural categories
    tab1, tab2, tab3 = st.tabs(["🎭 **Festivals**", "🏛️ **Heritage**", "💃 **Dance Forms**"])

    with tab1:
        show_festival_highlights(festivals_df)

    with tab2:
        show_heritage_highlights()

    with tab3:
        show_dance_highlights()

def show_festival_highlights(festivals_df):
    """Display festival highlights with enhanced visual design"""

    # Specific festivals to display
    target_festivals = ['Diwali', 'Durga Puja', 'Holi']

    # Filter festivals to show only the specified ones
    if not festivals_df.empty:
        highlight_festivals = festivals_df[festivals_df['FESTIVAL_NAME'].isin(target_festivals)]
        # If not found, try case-insensitive matching
        if highlight_festivals.empty:
            highlight_festivals = festivals_df[festivals_df['FESTIVAL_NAME'].str.lower().isin([f.lower() for f in target_festivals])]
        # If still empty, create fallback data
        if highlight_festivals.empty:
            fallback_data = []
            for festival in target_festivals:
                fallback_data.append({
                    'FESTIVAL_NAME': festival,
                    'STATE': 'All India',
                    'MONTH_SEASON': 'Various',
                    'DESCRIPTION': f'{festival} is one of the most celebrated festivals in India, bringing joy and unity across the nation.'
                })
            highlight_festivals = pd.DataFrame(fallback_data)
    else:
        # Create fallback data when no festivals_df is available
        fallback_data = []
        for festival in target_festivals:
            fallback_data.append({
                'FESTIVAL_NAME': festival,
                'STATE': 'All India',
                'MONTH_SEASON': 'Various',
                'DESCRIPTION': f'{festival} is one of the most celebrated festivals in India, bringing joy and unity across the nation.'
            })
        highlight_festivals = pd.DataFrame(fallback_data)

    # Create enhanced festival cards
    cols = st.columns(3)

    for idx, festival in enumerate(highlight_festivals.iterrows()):
        col_idx = idx % 3
        festival_data = festival[1]

        with cols[col_idx]:
            # Create enhanced festival card
            festival_name = festival_data['FESTIVAL_NAME'].replace(' ', '_').lower()
            possible_images = [
                f"Images/Festivals_images/{festival_name}-national.jpg",
                f"Images/Festivals_images/{festival_name}-national.jpeg",
                f"Images/Festivals_images/{festival_name}.jpg",
                f"Images/Festivals_images/{festival_name}.jpeg",
                f"Images/Festivals_images/{festival_data['FESTIVAL_NAME']}.jpg",
                f"Images/Festivals_images/{festival_data['FESTIVAL_NAME']}.jpeg",
                f"Images/Festivals_images/{festival_data['FESTIVAL_NAME'].replace(' ', '_')}.jpg",
                f"Images/Festivals_images/{festival_data['FESTIVAL_NAME'].replace(' ', '_')}.jpeg"
            ]

            image_found = False
            image_html = ""

            for img_path in possible_images:
                if os.path.exists(img_path):
                    try:
                        img = Image.open(img_path)
                        # Convert image to base64 for embedding
                        import base64
                        import io

                        # Resize image
                        img.thumbnail((400, 250), Image.Resampling.LANCZOS)

                        # Convert to base64
                        buffered = io.BytesIO()
                        img.save(buffered, format="JPEG")
                        img_str = base64.b64encode(buffered.getvalue()).decode()

                        image_html = f'<img src="data:image/jpeg;base64,{img_str}" class="festival-card-image" alt="{festival_data["FESTIVAL_NAME"]}">'
                        image_found = True
                        break
                    except:
                        continue

            if not image_found:
                # Create enhanced placeholder
                image_html = f"""
                <div class="festival-card-placeholder">
                    <div class="placeholder-icon">🎪</div>
                    <div class="placeholder-text">Festival Image</div>
                </div>
                """

            # Enhanced festival card with animations and better styling
            st.markdown(f"""
            <div class="enhanced-festival-card">
                <div class="festival-card-header">
                    {image_html}
                    <div class="festival-card-overlay">
                        <div class="festival-card-category">🎭 Festival</div>
                    </div>
                </div>
                <div class="festival-card-content">
                    <h4 class="festival-card-title">{festival_data['FESTIVAL_NAME']}</h4>
                    <div class="festival-card-details">
                        <div class="festival-detail-item">
                            <span class="detail-icon">📍</span>
                            <span class="detail-text">{festival_data['STATE']}</span>
                        </div>
                        <div class="festival-detail-item">
                            <span class="detail-icon">📅</span>
                            <span class="detail-text">{festival_data['MONTH_SEASON']}</span>
                        </div>
                    </div>
                    <p class="festival-card-description">
                        {festival_data['DESCRIPTION'][:120]}...
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)

def show_heritage_highlights():
    """Display heritage site highlights"""

    heritage_sites = [
        {
            "name": "Taj Mahal",
            "location": "Agra, Uttar Pradesh",
            "type": "Mausoleum",
            "description": "Ivory-white marble mausoleum, symbol of eternal love.",
            "icon": "🕌",
            "image_path": "Images/heritage_images/Agra_TAJ_MAHAL.jpg"
        },
        {
            "name": "Red Fort",
            "location": "Delhi",
            "type": "Fort Complex",
            "description": "Historic Mughal palace showcasing Indo-Islamic architecture.",
            "icon": "🏰",
            "image_path": "Images/heritage_images/Agra_RED_FORT.jpg"
        },
        {
            "name": "Thanjavur Temple",
            "location": "Tamil Nadu",
            "type": "Temple Complex",
            "description": "Magnificent Chola architecture and ancient Tamil temple art.",
            "icon": "🛕",
            "image_path": "Images/heritage_images/Thanjavur_Bragadeeswarar_Temple.jpg"
        }
    ]

    cols = st.columns(3)

    for idx, site in enumerate(heritage_sites):
        col_idx = idx % 3

        with cols[col_idx]:
            # Try to load and display heritage image
            image_html = ""
            if os.path.exists(site['image_path']):
                try:
                    img = Image.open(site['image_path'])
                    # Convert image to base64 for embedding
                    import base64
                    import io

                    # Resize image
                    img.thumbnail((400, 250), Image.Resampling.LANCZOS)

                    # Convert to base64
                    buffered = io.BytesIO()
                    img.save(buffered, format="JPEG")
                    img_str = base64.b64encode(buffered.getvalue()).decode()

                    image_html = f'<img src="data:image/jpeg;base64,{img_str}" class="heritage-card-image" alt="{site["name"]}">'
                except:
                    # Fallback to icon
                    image_html = f"""
                    <div class="heritage-icon-container">
                        <span class="heritage-icon">{site['icon']}</span>
                    </div>
                    """
            else:
                # Fallback to icon
                image_html = f"""
                <div class="heritage-icon-container">
                    <span class="heritage-icon">{site['icon']}</span>
                </div>
                """

            st.markdown(f"""
            <div class="enhanced-heritage-card">
                <div class="heritage-card-header">
                    {image_html}
                    <div class="heritage-card-overlay">
                        <div class="heritage-card-category">🏛️ Heritage</div>
                    </div>
                </div>
                <div class="heritage-card-content">
                    <h4 class="heritage-card-title">{site['name']}</h4>
                    <div class="heritage-card-details">
                        <div class="heritage-detail-item">
                            <span class="detail-icon">📍</span>
                            <span class="detail-text">{site['location']}</span>
                        </div>
                        <div class="heritage-detail-item">
                            <span class="detail-icon">🏗️</span>
                            <span class="detail-text">{site['type']}</span>
                        </div>
                    </div>
                    <p class="heritage-card-description">
                        {site['description']}
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)

def show_dance_highlights():
    """Display dance form highlights"""

    dance_forms = [
        {
            "name": "Bharatanatyam",
            "origin": "Tamil Nadu",
            "style": "Classical",
            "description": "Ancient classical dance expressing devotion through movements.",
            "icon": "💃",
            "image_path": "Images/dance_photos/tamil_nadu_bharatanatyam.jpg"
        },
        {
            "name": "Kathakali",
            "origin": "Kerala",
            "style": "Classical",
            "description": "Dramatic dance-drama with elaborate costumes and storytelling.",
            "icon": "🎭",
            "image_path": "Images/dance_photos/kerala_kathakali.jpg"
        },
        {
            "name": "Odissi",
            "origin": "Odisha",
            "style": "Classical",
            "description": "Sculptural dance inspired by temple carvings and fluid movements.",
            "icon": "🌊",
            "image_path": "Images/dance_photos/odisha_odissi.jpg"
        }
    ]

    cols = st.columns(3)

    for idx, dance in enumerate(dance_forms):
        col_idx = idx % 3

        with cols[col_idx]:
            # Try to load and display dance image
            image_html = ""
            if os.path.exists(dance['image_path']):
                try:
                    img = Image.open(dance['image_path'])
                    # Convert image to base64 for embedding
                    import base64
                    import io

                    # Resize image
                    img.thumbnail((400, 250), Image.Resampling.LANCZOS)

                    # Convert to base64
                    buffered = io.BytesIO()
                    img.save(buffered, format="JPEG")
                    img_str = base64.b64encode(buffered.getvalue()).decode()

                    image_html = f'<img src="data:image/jpeg;base64,{img_str}" class="dance-card-image" alt="{dance["name"]}">'
                except:
                    # Fallback to icon
                    image_html = f"""
                    <div class="dance-icon-container">
                        <span class="dance-icon">{dance['icon']}</span>
                    </div>
                    """
            else:
                # Fallback to icon
                image_html = f"""
                <div class="dance-icon-container">
                    <span class="dance-icon">{dance['icon']}</span>
                </div>
                """

            st.markdown(f"""
            <div class="enhanced-dance-card">
                <div class="dance-card-header">
                    {image_html}
                    <div class="dance-card-overlay">
                        <div class="dance-card-category">💃 Dance</div>
                    </div>
                </div>
                <div class="dance-card-content">
                    <h4 class="dance-card-title">{dance['name']}</h4>
                    <div class="dance-card-details">
                        <div class="dance-detail-item">
                            <span class="detail-icon">📍</span>
                            <span class="detail-text">{dance['origin']}</span>
                        </div>
                        <div class="dance-detail-item">
                            <span class="detail-icon">🎨</span>
                            <span class="detail-text">{dance['style']}</span>
                        </div>
                    </div>
                    <p class="dance-card-description">
                        {dance['description']}
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
