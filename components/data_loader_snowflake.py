import streamlit as st
import pandas as pd

def get_snowflake_connection():
    """Get Snowflake connection"""
    return st.connection("snowflake")

@st.cache_data
def load_festivals_data():
    """Load festivals data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.CULTURAL_DATA.FESTIVAL")
    except Exception as e:
        st.error(f"Error loading festivals data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_dance_data():
    """Load dance forms data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.CULTURAL_DATA.DANCE_FORMS")
    except Exception as e:
        st.error(f"Error loading dance data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_ita_data():
    """Load International Tourist Arrivals data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.ITA_YEARLY")
    except Exception as e:
        st.error(f"Error loading ITA data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_ita_monthly_data():
    """Load monthly ITA data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.ITA_MONTHLY")
    except Exception as e:
        st.error(f"Error loading monthly ITA data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_state_tourism_data():
    """Load state-wise tourism data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.STATE_WISE_TOURIST")
    except Exception as e:
        st.error(f"Error loading state tourism data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_centrally_protected_data():
    """Load centrally protected monuments data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.CENTRALLY_PROTECTED")
    except Exception as e:
        st.error(f"Error loading centrally protected data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_duration_stay_data():
    """Load tourist duration stay data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.DURATION_STAY")
    except Exception as e:
        st.error(f"Error loading duration stay data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_fee_earnings_data():
    """Load foreign exchange earnings data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.FEE_EARNINGS")
    except Exception as e:
        st.error(f"Error loading fee earnings data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_india_world_share_data():
    """Load India's world tourism share data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.INDIA_WORLD_SHARE")
    except Exception as e:
        st.error(f"Error loading India world share data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_lean_peak_data():
    """Load lean and peak month data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.LEAN_PEAK_MONTH")
    except Exception as e:
        st.error(f"Error loading lean peak data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_monthly_foreigners_data():
    """Load monthly foreigners arrival data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.MONTHLY_FOREIGNERS")
    except Exception as e:
        st.error(f"Error loading monthly foreigners data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_state_footfall_data():
    """Load state-wise footfall data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.STATE_FOOTFALL")
    except Exception as e:
        st.error(f"Error loading state footfall data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_top_monuments_data():
    """Load top 10 monuments data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.TOP_MONUMENTS")
    except Exception as e:
        st.error(f"Error loading top monuments data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_age_statistics_data():
    """Load age-wise tourism statistics data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.AGE_STATISTICS")
    except Exception as e:
        st.error(f"Error loading age statistics data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_tourism_gdp_data():
    """Load tourism GDP contribution data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.TOURISM_GDP")
    except Exception as e:
        st.error(f"Error loading tourism GDP data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_tourism_employment_data():
    """Load tourism employment data from Snowflake"""
    try:
        conn = get_snowflake_connection()
        return conn.query("SELECT * FROM CULTURE_TOURISM_DB.TOURISM_DATA.TOURISM_EMPLOYMENT")
    except Exception as e:
        st.error(f"Error loading tourism employment data: {e}")
        return pd.DataFrame()

# Image loading functions for Snowflake stages
@st.cache_data
def get_image_url_from_stage(stage_name, file_path):
    """Get presigned URL for image in Snowflake stage"""
    try:
        conn = get_snowflake_connection()
        query = f"SELECT GET_PRESIGNED_URL('@{stage_name}', '{file_path}') as image_url"
        result = conn.query(query)
        if not result.empty:
            return result.iloc[0]['IMAGE_URL']
        return None
    except Exception as e:
        st.error(f"Error getting image URL: {e}")
        return None

@st.cache_data
def get_available_images(stage_name):
    """Get list of all images in a stage"""
    try:
        conn = get_snowflake_connection()
        query = f"LIST '@{stage_name}'"
        result = conn.query(query)
        if not result.empty:
            return result['name'].tolist()
        return []
    except Exception as e:
        st.error(f"Error listing images: {e}")
        return []

def get_festival_image_url(festival_name):
    """Get festival image URL from Snowflake stage"""
    try:
        # Try different image formats
        for ext in ['.jpg', '.jpeg', '.png']:
            file_name = f"{festival_name.replace(' ', '_')}{ext}"
            image_url = get_image_url_from_stage('CULTURE_TOURISM_DB.ASSETS.FESTIVAL_IMAGES', file_name)
            if image_url:
                return image_url
        return None
    except Exception as e:
        return None

def get_dance_image_url(state_name, dance_name):
    """Get dance image URL from Snowflake stage"""
    try:
        # Try different naming conventions
        for ext in ['.jpg', '.jpeg', '.png']:
            file_name = f"{state_name.lower().replace(' ', '_')}_{dance_name.lower().replace(' ', '_')}{ext}"
            image_url = get_image_url_from_stage('CULTURE_TOURISM_DB.ASSETS.DANCE_IMAGES', file_name)
            if image_url:
                return image_url
        return None
    except Exception as e:
        return None

def get_heritage_image_url(city_name, heritage_name):
    """Get heritage image URL from Snowflake stage"""
    try:
        # Try different naming conventions
        for ext in ['.jpg', '.jpeg', '.png']:
            file_name = f"{city_name.upper()}_{heritage_name.replace(' ', '_')}{ext}"
            image_url = get_image_url_from_stage('CULTURE_TOURISM_DB.ASSETS.HERITAGE_IMAGES', file_name)
            if image_url:
                return image_url
        return None
    except Exception as e:
        return None

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
