import streamlit as st
import pandas as pd

# Import components
from components.data_loader import load_all_data
from components.homepage import show_homepage
from components.festivals import show_festivals_section
from components.dance_forms import show_dance_section
from components.heritage_sites import show_heritage_section
from components.tourism_analytics import show_tourism_analytics
from styles.css_styles import apply_custom_css, apply_dance_styles, apply_sidebar_styles

# Page configuration
st.set_page_config(
    page_title="Indian Cultural Heritage & Tourism",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply CSS styles
apply_custom_css()
apply_dance_styles()
apply_sidebar_styles()

def show_art_forms(festivals_df, dance_df, heritage_sites_df, unesco_df):
    """Display traditional art forms section"""
    st.markdown('<h1 class="main-header">🎭 Traditional Art Forms</h1>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🎪 Festivals", "💃 Dance Forms", "🏛️ Heritage Sites"])

    with tab1:
        show_festivals_section(festivals_df)

    with tab2:
        show_dance_section(dance_df)

    with tab3:
        show_heritage_section()

def main():
    # Clear cache button for development
    if st.sidebar.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()

    # Sidebar navigation
    st.sidebar.markdown("# 🏛️ Navigation")
    page = st.sidebar.selectbox(
        "Choose a section:",
        [
            "🏠 Home",
            "🎭 Traditional Art Forms",
            "📊 Tourism Analytics"
        ]
    )

    # Load all data using the data loader
    data = load_all_data()

    if page == "🏠 Home":
        show_homepage(
            data['festivals_df'],
            data['ita_df'],
            data['state_tourism_df'],
            data['tourism_gdp_df'],
            data['tourism_employment_df']
        )
    elif page == "🎭 Traditional Art Forms":
        show_art_forms(
            data['festivals_df'],
            data['dance_df'],
            data['heritage_sites_df'],
            data['unesco_df']
        )
    elif page == "📊 Tourism Analytics":
        show_tourism_analytics(
            data['ita_df'], data['ita_monthly_df'], data['state_tourism_df'],
            data['centrally_protected_domestic_df'], data['duration_stay_df'], data['fee_earnings_df'],
            data['india_world_share_df'], data['lean_peak_df'], data.get('state_foreign_tourism_df', pd.DataFrame()),
            data.get('top_monuments_domestic_df', pd.DataFrame()), data.get('top_monuments_foreign_df', pd.DataFrame()), data['age_statistics_df'],
            data['tourism_gdp_df'], data['tourism_employment_df']
        )

if __name__ == "__main__":
    main()
