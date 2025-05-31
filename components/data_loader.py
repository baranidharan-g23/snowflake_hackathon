import streamlit as st
import pandas as pd
import os
import glob

@st.cache_data
def load_festivals_data():
    """Load festivals data"""
    try:
        return pd.read_csv('Datasets/Festivals.csv')
    except FileNotFoundError:
        st.error("Datasets/Festivals.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_dance_data():
    """Load dance forms data"""
    try:
        return pd.read_csv('Datasets/dance.csv')
    except FileNotFoundError:
        st.error("Datasets/dance.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_heritage_sites_data():
    """Load heritage sites data"""
    try:
        return pd.read_csv('Datasets/heritage_sites.csv')
    except FileNotFoundError:
        st.error("Datasets/heritage_sites.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_unesco_data():
    """Load UNESCO World Heritage Sites data"""
    try:
        return pd.read_csv('Datasets/Unesco.csv')
    except FileNotFoundError:
        st.error("Datasets/Unesco.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_ita_data():
    """Load International Tourist Arrivals data"""
    try:
        return pd.read_csv('Datasets/ITA_YEARLY.csv')
    except FileNotFoundError:
        st.error("Datasets/ITA_YEARLY.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_ita_monthly_data():
    """Load monthly ITA data"""
    try:
        return pd.read_csv('Datasets/ITA_MONTHLY.csv')
    except FileNotFoundError:
        st.error("Datasets/ITA_MONTHLY.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_state_tourism_data():
    """Load state-wise tourism data - prioritize total arrivals dataset"""
    try:
        # Try total arrivals first (preferred), then tourist arrivals as fallback
        for filename in ['State_Wise_Total_Tourist_Arrivals_2017_2023.csv',
                        'State_Wise_Domestic_Tourist_Arrivals_2017_2023.csv']:
            filepath = f'Datasets/{filename}'
            if os.path.exists(filepath):
                return pd.read_csv(filepath)
        st.error("State tourism data files not found!")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading state tourism data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_state_foreign_tourism_data():
    """Load state-wise foreign tourist arrivals data"""
    try:
        return pd.read_csv('Datasets/State_Wise_Foreign_Tourist_Arrivals_2017_2023.csv')
    except FileNotFoundError:
        st.error("Datasets/State_Wise_Foreign_Tourist_Arrivals_2017_2023.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_centrally_protected_domestic_data():
    """Load centrally protected monuments domestic visits data"""
    try:
        return pd.read_csv('Datasets/Centrally_Protected_Monuments_Domestic_Visits_2019_2024.csv')
    except FileNotFoundError:
        st.error("Datasets/Centrally_Protected_Monuments_Domestic_Visits_2019_2024.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_centrally_protected_foreign_data():
    """Load centrally protected monuments foreign visits data"""
    try:
        return pd.read_csv('Datasets/Centrally_Protected_Monuments_Foreign_Visits_2019_2024.csv.csv')
    except FileNotFoundError:
        st.error("Datasets/Centrally_Protected_Monuments_Foreign_Visits_2019_2024.csv.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_top_monuments_domestic_data():
    """Load top 10 monuments domestic visits data"""
    try:
        return pd.read_csv('Datasets/Top_10_Monuments_Domestic_Visits_2019_2024.csv')
    except FileNotFoundError:
        st.error("Datasets/Top_10_Monuments_Domestic_Visits_2019_2024.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_top_monuments_foreign_data():
    """Load top 10 monuments foreign visits data"""
    try:
        return pd.read_csv('Datasets/Top_10_Monuments_Foreign_Visits_2019_2024.csv')
    except FileNotFoundError:
        st.error("Datasets/Top_10_Monuments_Foreign_Visits_2019_2024.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_duration_stay_data():
    """Load tourist duration stay data"""
    try:
        return pd.read_csv('Datasets/Stay_Duration_2017_2023.csv')
    except FileNotFoundError:
        st.error("Datasets/Stay_Duration_2017_2023.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_fee_earnings_data():
    """Load foreign exchange earnings data"""
    try:
        return pd.read_csv('Datasets/FEE_EARNINGS_2011-2023.csv')
    except FileNotFoundError:
        st.error("Datasets/FEE_EARNINGS_2011-2023.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_india_world_share_data():
    """Load India's world tourism share data"""
    try:
        return pd.read_csv('Datasets/India_Share_World_2001_2021.csv')
    except FileNotFoundError:
        st.error("Datasets/India_Share_World_2001_2021.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_lean_peak_data():
    """Load lean and peak month data - combines all years"""
    try:
        # Load all lean peak month files
        lean_peak_files = glob.glob('Datasets/Lean_Peak_Months/*.csv')
        if not lean_peak_files:
            st.error("No lean peak month files found!")
            return pd.DataFrame()

        all_data = []
        for file in lean_peak_files:
            year = os.path.basename(file).split('_')[0]
            df = pd.read_csv(file)
            df['YEAR'] = year
            all_data.append(df)

        return pd.concat(all_data, ignore_index=True)
    except Exception as e:
        st.error(f"Error loading lean peak data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_age_statistics_data():
    """Load age-wise tourism statistics data"""
    try:
        return pd.read_csv('Datasets/India-Tourism-Statistics-age-2001-2020.csv')
    except FileNotFoundError:
        st.error("Datasets/India-Tourism-Statistics-age-2001-2020.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_tourism_gdp_data():
    """Load tourism GDP contribution data"""
    try:
        return pd.read_csv('Datasets/Tourism_Share_GDP.csv')
    except FileNotFoundError:
        st.error("Datasets/Tourism_Share_GDP.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_tourism_employment_data():
    """Load tourism employment data"""
    try:
        return pd.read_csv('Datasets/Tourism_Employment.csv')
    except FileNotFoundError:
        st.error("Datasets/Tourism_Employment.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_centrally_protected_domestic_data():
    """Load centrally protected monuments domestic visits data"""
    try:
        return pd.read_csv('Datasets/Centrally_Protected_Monuments_Domestic_Visits_2019_2024.csv')
    except FileNotFoundError:
        st.error("Datasets/Centrally_Protected_Monuments_Domestic_Visits_2019_2024.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_centrally_protected_foreign_data():
    """Load centrally protected monuments foreign visits data"""
    try:
        return pd.read_csv('Datasets/Centrally_Protected_Monuments_Foreign_Visits_2019_2024.csv.csv')
    except FileNotFoundError:
        st.error("Datasets/Centrally_Protected_Monuments_Foreign_Visits_2019_2024.csv.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_top_monuments_domestic_data():
    """Load top 10 monuments domestic visits data"""
    try:
        return pd.read_csv('Datasets/Top_10_Monuments_Domestic_Visits_2019_2024.csv')
    except FileNotFoundError:
        st.error("Datasets/Top_10_Monuments_Domestic_Visits_2019_2024.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_top_monuments_foreign_data():
    """Load top 10 monuments foreign visits data"""
    try:
        return pd.read_csv('Datasets/Top_10_Monuments_Foreign_Visits_2019_2024.csv')
    except FileNotFoundError:
        st.error("Datasets/Top_10_Monuments_Foreign_Visits_2019_2024.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_lean_peak_data_by_year(year):
    """Load lean peak months data for a specific year"""
    try:
        return pd.read_csv(f'Datasets/Lean_Peak_Months/{year}_Lean_Peak_Month.csv')
    except FileNotFoundError:
        st.error(f"Datasets/Lean_Peak_Months/{year}_Lean_Peak_Month.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_all_lean_peak_data():
    """Load all lean peak months data from 2017-2023"""
    all_data = {}
    for year in range(2017, 2024):
        all_data[year] = load_lean_peak_data_by_year(year)
    return all_data

def clear_dance_cache():
    """Clear the cache for dance data"""
    load_dance_data.clear()

def clear_all_cache():
    """Clear all cached data"""
    load_festivals_data.clear()
    load_dance_data.clear()
    load_heritage_sites_data.clear()
    load_unesco_data.clear()
    load_ita_data.clear()
    load_ita_monthly_data.clear()
    load_state_tourism_data.clear()
    load_state_foreign_tourism_data.clear()
    load_centrally_protected_domestic_data.clear()
    load_centrally_protected_foreign_data.clear()
    load_top_monuments_domestic_data.clear()
    load_top_monuments_foreign_data.clear()
    load_duration_stay_data.clear()
    load_fee_earnings_data.clear()
    load_india_world_share_data.clear()
    load_lean_peak_data.clear()
    load_age_statistics_data.clear()
    load_tourism_gdp_data.clear()
    load_tourism_employment_data.clear()

def load_all_data():
    """Load all data and return as a dictionary"""
    return {
        'festivals_df': load_festivals_data(),
        'dance_df': load_dance_data(),
        'heritage_sites_df': load_heritage_sites_data(),
        'unesco_df': load_unesco_data(),
        'ita_df': load_ita_data(),
        'ita_monthly_df': load_ita_monthly_data(),
        'state_tourism_df': load_state_tourism_data(),
        'state_foreign_tourism_df': load_state_foreign_tourism_data(),
        'centrally_protected_domestic_df': load_centrally_protected_domestic_data(),
        'centrally_protected_foreign_df': load_centrally_protected_foreign_data(),
        'top_monuments_domestic_df': load_top_monuments_domestic_data(),
        'top_monuments_foreign_df': load_top_monuments_foreign_data(),
        'duration_stay_df': load_duration_stay_data(),
        'fee_earnings_df': load_fee_earnings_data(),
        'india_world_share_df': load_india_world_share_data(),
        'lean_peak_df': load_lean_peak_data(),  # Load combined data
        'all_lean_peak_df': load_all_lean_peak_data(),
        'age_statistics_df': load_age_statistics_data(),
        'tourism_gdp_df': load_tourism_gdp_data(),
        'tourism_employment_df': load_tourism_employment_data()
    }



