import streamlit as st
import pandas as pd

@st.cache_data
def load_festivals_data():
    """Load festivals data"""
    try:
        return pd.read_csv('Festivals.csv')
    except FileNotFoundError:
        st.error("Festivals.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_dance_data():
    """Load dance forms data"""
    try:
        return pd.read_csv('dance_final.csv')
    except FileNotFoundError:
        st.error("dance_final.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_ita_data():
    """Load International Tourist Arrivals data"""
    try:
        return pd.read_csv('ITA_YEARLY.csv')
    except FileNotFoundError:
        st.error("ITAs(1-23).csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_ita_monthly_data():
    """Load monthly ITA data"""
    try:
        return pd.read_csv('ITA_MONTHLY.csv')
    except FileNotFoundError:
        st.error("ITAs(21-23)_Month_wise.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_state_tourism_data():
    """Load state-wise tourism data"""
    try:
        return pd.read_csv('State_wise_tourist_2022_2023.csv')
    except FileNotFoundError:
        st.error("State_wise_tourist_2022_2023.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_centrally_protected_data():
    """Load centrally protected monuments data"""
    try:
        return pd.read_csv('CENTRALLY_PROTECTED_19-20-21.csv')
    except FileNotFoundError:
        st.error("CENTRALLY_PROTECTED_19-20-21.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_duration_stay_data():
    """Load tourist duration stay data"""
    try:
        # Load CSV without headers and assign proper column names
        df = pd.read_csv('DURATION_STAY_2017.csv', header=None)
        df.columns = ['Region', 'Nationality', 'Average duration of stay (in days)']
        return df
    except FileNotFoundError:
        st.error("DURATION_STAY_2017.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_fee_earnings_data():
    """Load foreign exchange earnings data"""
    try:
        # Try different encodings
        for encoding in ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']:
            try:
                return pd.read_csv('FEE_EARNINGS91-2020.csv', encoding=encoding)
            except UnicodeDecodeError:
                continue
        # If all encodings fail, return empty DataFrame
        st.warning("Could not read fee earnings data due to encoding issues")
        return pd.DataFrame()
    except FileNotFoundError:
        st.error("FEE_EARNINGS91-2020.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_india_world_share_data():
    """Load India's world tourism share data"""
    try:
        # Try different encodings
        for encoding in ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']:
            try:
                return pd.read_csv('INDIA_SHARE_ON_WOLRD01-21.csv', encoding=encoding)
            except UnicodeDecodeError:
                continue
        # If all encodings fail, return empty DataFrame
        st.warning("Could not read India world share data due to encoding issues")
        return pd.DataFrame()
    except FileNotFoundError:
        st.error("INDIA_SHARE_ON_WOLRD01-21.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_lean_peak_data():
    """Load lean and peak month data"""
    try:
        return pd.read_csv('LEAN_PEAK_MONTH_FTA_2017.csv')
    except FileNotFoundError:
        st.error("LEAN_PEAK_MONTH_FTA_2017.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_monthly_foreigners_data():
    """Load monthly foreigners arrival data"""
    try:
        return pd.read_csv('MONTHLY_FOREIGNERS_ARRIVAL23-24.csv')
    except FileNotFoundError:
        st.error("MONTHLY_FOREIGNERS_ARRIVAL23-24.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_state_footfall_data():
    """Load state-wise footfall data"""
    try:
        return pd.read_csv('STATE_WISE_FOOTFALL20_22.csv')
    except FileNotFoundError:
        st.error("STATE_WISE_FOOTFALL20_22.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_top_monuments_data():
    """Load top 10 monuments data"""
    try:
        return pd.read_csv('TOP_10_MONUMENTS.csv')
    except FileNotFoundError:
        st.error("TOP_10_MONUMENTS.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_age_statistics_data():
    """Load age-wise tourism statistics data"""
    try:
        return pd.read_csv('India-Tourism-Statistics-age-2001-2020.csv')
    except FileNotFoundError:
        st.error("India-Tourism-Statistics-age-2001-2020.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_tourism_gdp_data():
    """Load tourism GDP contribution data"""
    try:
        return pd.read_csv('Tourism_Share_GDP_GVP.csv')
    except FileNotFoundError:
        st.error("Tourism_Share_GDP_GVP.csv file not found!")
        return pd.DataFrame()

@st.cache_data
def load_tourism_employment_data():
    """Load tourism employment data"""
    try:
        return pd.read_csv('Tourism_Employment.csv')
    except FileNotFoundError:
        st.error("Tourism_Employment.csv file not found!")
        return pd.DataFrame()

def clear_dance_cache():
    """Clear the cache for dance data"""
    load_dance_data.clear()

def load_all_data():
    """Load all data and return as a dictionary"""
    return {
        'festivals_df': load_festivals_data(),
        'dance_df': load_dance_data(),
        'ita_df': load_ita_data(),
        'ita_monthly_df': load_ita_monthly_data(),
        'state_tourism_df': load_state_tourism_data(),
        'centrally_protected_df': load_centrally_protected_data(),
        'duration_stay_df': load_duration_stay_data(),
        'fee_earnings_df': load_fee_earnings_data(),
        'india_world_share_df': load_india_world_share_data(),
        'lean_peak_df': load_lean_peak_data(),
        'monthly_foreigners_df': load_monthly_foreigners_data(),
        'state_footfall_df': load_state_footfall_data(),
        'top_monuments_df': load_top_monuments_data(),
        'age_statistics_df': load_age_statistics_data(),
        'tourism_gdp_df': load_tourism_gdp_data(),
        'tourism_employment_df': load_tourism_employment_data()
    }



