import streamlit as st
import pandas as pd

# Import components
from components.data_loader import (
    load_all_data, load_unesco_data, load_top_monuments_domestic_data, load_top_monuments_foreign_data,
    load_centrally_protected_domestic_data, load_centrally_protected_foreign_data,
    load_tourism_gdp_data, load_tourism_employment_data, load_fee_earnings_data,
    load_india_world_share_data, load_ita_data, load_ita_monthly_data,
    load_duration_stay_data, load_age_statistics_data, load_all_lean_peak_data,
    load_state_tourism_data, load_state_foreign_tourism_data
)
from components.homepage import show_homepage
from components.festivals import show_festivals_section
from components.dance_forms import show_dance_section
from components.heritage_sites import show_heritage_section
from components.chapter1_heritage_heartbeat import show_heritage_heartbeat
from components.chapter2_economic_multiplier import show_economic_multiplier
from components.chapter3_travelers_journey import show_travelers_journey
from components.chapter4_regional_tapestry import show_regional_tapestry
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
            "🏛️ Chapter 1: Heritage Heartbeat",
            "💰 Chapter 2: Economic Multiplier",
            "🌍 Chapter 3: Traveler's Journey",
            "🗺️ Chapter 4: Regional Tapestry"
        ]
    )

    # Load all data using the data loader (for existing components)
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
    elif page == "🏛️ Chapter 1: Heritage Heartbeat":
        # Load heritage data
        unesco_df = load_unesco_data()
        top_monuments_domestic_df = load_top_monuments_domestic_data()
        top_monuments_foreign_df = load_top_monuments_foreign_data()
        centrally_protected_domestic_df = load_centrally_protected_domestic_data()
        centrally_protected_foreign_df = load_centrally_protected_foreign_data()

        show_heritage_heartbeat(
            unesco_df,
            top_monuments_domestic_df,
            top_monuments_foreign_df,
            centrally_protected_domestic_df,
            centrally_protected_foreign_df
        )

    elif page == "💰 Chapter 2: Economic Multiplier":
        # Load economic data
        tourism_gdp_df = load_tourism_gdp_data()
        tourism_employment_df = load_tourism_employment_data()
        fee_earnings_df = load_fee_earnings_data()
        india_world_share_df = load_india_world_share_data()

        show_economic_multiplier(
            tourism_gdp_df,
            tourism_employment_df,
            fee_earnings_df,
            india_world_share_df
        )

    elif page == "🌍 Chapter 3: Traveler's Journey":
        # Load traveler data
        ita_df = load_ita_data()
        ita_monthly_df = load_ita_monthly_data()
        stay_duration_df = load_duration_stay_data()
        age_statistics_df = load_age_statistics_data()
        all_lean_peak_data = load_all_lean_peak_data()

        show_travelers_journey(
            ita_df,
            ita_monthly_df,
            stay_duration_df,
            age_statistics_df,
            all_lean_peak_data
        )

    elif page == "🗺️ Chapter 4: Regional Tapestry":
        # Load regional tourism data only
        state_total_df = load_state_tourism_data()  # This loads total arrivals
        state_foreign_df = load_state_foreign_tourism_data()

        # Load domestic data separately
        try:
            state_domestic_df = pd.read_csv('Datasets/State_Wise_Domestic_Tourist_Arrivals_2017_2023.csv')
        except:
            state_domestic_df = pd.DataFrame()

        show_regional_tapestry(
            state_total_df,
            state_domestic_df,
            state_foreign_df
        )

if __name__ == "__main__":
    main()
