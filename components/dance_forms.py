import streamlit as st
import pandas as pd
import os
from PIL import Image
from .data_loader import clear_dance_cache

@st.cache_data
def load_and_cache_dance_image(image_path):
    """Load and cache dance image to avoid repeated file system calls"""
    if os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            return image
        except Exception as e:
            st.error(f"Error loading dance image {image_path}: {e}")
            return None
    return None

@st.cache_data
def get_dance_image_info(image_path):
    """Cache dance image existence and basic info"""
    if os.path.exists(image_path):
        try:
            with Image.open(image_path) as img:
                return {"exists": True, "size": img.size, "format": img.format}
        except:
            return {"exists": False, "size": None, "format": None}
    return {"exists": False, "size": None, "format": None}

def show_dance_section(dance_df):
    """Display enhanced dance forms information with slideshow and Indian dance information"""
    st.markdown('<h2 class="section-header">🗺️ Explore Dance Forms by State</h2>', unsafe_allow_html=True)

    if dance_df.empty:
        st.warning("No dance data available")
        return

    selected_state = st.selectbox(
        "Select a State to explore its dance traditions:",
        ["Highlights"] + sorted(list(dance_df['STATE'].unique())),
        key="dance_state_selector"
    )

    if selected_state != "Highlights":
        # Show featured state layout
        show_featured_state_dances(dance_df, selected_state)
    else:
        # Show automatic slideshow and Indian dance info when "Classical Dance Forms" is selected
        show_automatic_dance_slideshow(dance_df)
        show_indian_dance_info()

def show_automatic_dance_slideshow(dance_df):
    """Simple elegant slideshow displaying classical dance forms"""
    # Filter to show only the classical dances including Kathak
    classical_dances = ['Bharatanatyam', 'Kuchipudi', 'Kathakali', 'Odissi', 'Manipuri', 'Mohiniyattam', 'Kathak']
    dances_with_images = dance_df[
        (dance_df['DOWNLOADED_DANCE_IMAGES'].notna()) &
        (dance_df['DOWNLOADED_DANCE_IMAGES'] != 'None') &
        (dance_df['FOLK_DANCE'].isin(classical_dances))
    ].copy()

    if dances_with_images.empty:
        st.warning("No classical dance images available for slideshow")
        return

    # Initialize session state for slideshow
    if 'slideshow_index' not in st.session_state:
        st.session_state.slideshow_index = 0

    # Ensure index is within bounds
    if st.session_state.slideshow_index >= len(dances_with_images):
        st.session_state.slideshow_index = 0

    # Get current dance
    current_dance = dances_with_images.iloc[st.session_state.slideshow_index]

    # Center the slideshow content
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Display image using cached loading
        img_path = f"Images/dance_photos/{current_dance['DOWNLOADED_DANCE_IMAGES']}"
        img = load_and_cache_dance_image(img_path)
        if img:
            try:
                # Create a copy for resizing to avoid modifying cached image
                img_copy = img.copy()
                # Always resize image to a consistent size (enlarge if needed)
                img_copy = img_copy.resize((800, 500), Image.Resampling.LANCZOS)
                st.image(img_copy, use_container_width=True)
            except Exception as e:
                st.error(f"Error processing image: {e}")
                show_dance_placeholder()
        else:
            show_dance_placeholder()

    # Simple navigation controls with better alignment
    st.markdown("<br>", unsafe_allow_html=True)

    # Create centered navigation container
    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns([2, 1, 1, 1, 2])

    with nav_col2:
        if st.button("◀", key="prev_dance", help="Previous dance", use_container_width=True):
            st.session_state.slideshow_index = (st.session_state.slideshow_index - 1) % len(dances_with_images)
            st.rerun()

    with nav_col3:
        st.markdown(f"""
        <div style="text-align: center; padding: 0.5rem; display: flex; align-items: center; justify-content: center; height: 38px;">
            <span style="color: white; font-weight: bold; font-size: 1.5rem;">
                {current_dance['FOLK_DANCE']}
            </span>
        </div>
        """, unsafe_allow_html=True)

    with nav_col4:
        if st.button("▶", key="next_dance", help="Next dance", use_container_width=True):
            st.session_state.slideshow_index = (st.session_state.slideshow_index + 1) % len(dances_with_images)
            st.rerun()

    # Add custom CSS for better button styling
    st.markdown("""
    <style>
    div[data-testid="column"]:nth-child(2) button,
    div[data-testid="column"]:nth-child(4) button {
        width: 50px !important;
        height: 38px !important;
        border-radius: 50% !important;
        background: #008080 !important;
        color: white !important;
        border: none !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 auto !important;
        transition: all 0.2s ease !important;
    }

    div[data-testid="column"]:nth-child(2) button:hover,
    div[data-testid="column"]:nth-child(4) button:hover {
        background: #20B2AA !important;
        transform: scale(1.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

def show_indian_dance_info():
    """Display general information about Indian Dance"""
    st.markdown('<h3 style="color: white; text-align: center; margin: 2rem 0; font-family: Playfair Display, serif; font-size: 2rem;">A Living Heritage of Expression and Devotion</h3>', unsafe_allow_html=True)

    # Main content in separate sections to avoid HTML parsing issues
    st.markdown("""
    <div style="background: rgba(255,255,255,0.9); padding: 2rem; border-radius: 15px;
                margin: 1rem 0; box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                border: 2px solid #008080;">
        <p style="font-size: 1.1rem; margin-bottom: 1.5rem; text-align: justify; line-height: 1.8; color: teal;">
            Indian dance is one of the world's oldest and most sophisticated performing arts traditions,
            representing a perfect synthesis of rhythm, melody, expression, and spirituality. With roots
            dating back over 2,000 years, Indian dance forms are not merely entertainment but are considered
            sacred arts that connect the performer and audience with the divine.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Create columns for the four sections
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background: #008080; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #008080; margin-bottom: 1rem;">
            <h5 style="color: white; margin-bottom: 0.5rem; font-size: 1.2rem;">🎭 Classical Traditions</h5>
            <p style="margin: 0; line-height: 1.6; color: white;">India recognizes eight classical dance forms: Bharatanatyam, Kathak, Kathakali,
            Kuchipudi, Odissi, Manipuri, Mohiniyattam, and Sattriya. Each follows the principles
            laid down in the ancient treatise Natya Shastra, emphasizing precise movements,
            expressions, and spiritual themes.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background: #008080; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #008080;">
            <h5 style="color: white; margin-bottom: 0.5rem; font-size: 1.2rem;">🙏 Spiritual Significance</h5>
            <p style="margin: 0; line-height: 1.6; color: white;">Indian dance is deeply rooted in spirituality, with many forms originating in
            temples as offerings to deities. The concept of dance as worship (Natya as Yoga)
            makes it a path to spiritual enlightenment and divine connection.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: #008080; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #008080; margin-bottom: 1rem;">
            <h5 style="color: white; margin-bottom: 0.5rem; font-size: 1.2rem;">🌾 Folk Expressions</h5>
            <p style="margin: 0; line-height: 1.6; color: white;">Beyond classical forms, India boasts hundreds of folk dances that celebrate
            agricultural cycles, seasonal changes, religious festivals, and community life.
            These dances reflect the diverse cultural landscape of different regions and communities properspering the wellness of people.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background: #008080; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #008080;">
            <h5 style="color: white; margin-bottom: 0.5rem; font-size: 1.2rem;">🌍 Global Influence</h5>
            <p style="margin: 0; line-height: 1.6; color: white;">Indian dance has influenced performing arts worldwide, with its emphasis on
            storytelling through movement, intricate hand gestures (mudras), and the integration
            of music, rhythm, and expression inspiring artists globally.</p>
        </div>
        """, unsafe_allow_html=True)

    # Quote section
    st.markdown("""
    <div style="background: linear-gradient(135deg, #008080, #20B2AA); color: white;
                padding: 1.5rem; border-radius: 10px; margin-top: 2rem; text-align: center;">
        <p style="font-size: 1.1rem; margin: 0; font-style: italic;">
            "Where the hand goes, the eyes follow; where the eyes go, the mind follows;<br>
            where the mind goes, there is expression; where there is expression, there is bliss."
        </p>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.9;">
            <em>- Ancient Sanskrit saying about dance</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_featured_state_dances(dance_df, selected_state):
    """Display featured state dance layout with main dance and descriptions"""

    # Get state data - get the first dance with a detailed description
    state_data = dance_df[dance_df['STATE'] == selected_state]

    if state_data.empty:
        st.warning(f"No dance data available for {selected_state}")
        return

    # Find the main dance - prioritize specific dances for certain states
    main_dance = None
    other_dances = []

    # Special handling for Uttar Pradesh - prioritize Kathak
    if selected_state == "Uttar Pradesh":
        kathak_dance = state_data[state_data['FOLK_DANCE'] == 'Kathak']
        if not kathak_dance.empty:
            main_dance = kathak_dance.iloc[0]
            # Add all other dances to other_dances
            for idx, dance_info in state_data.iterrows():
                if dance_info['FOLK_DANCE'] != 'Kathak':
                    other_dances.append(dance_info)
        else:
            # Fallback if Kathak not found
            main_dance = state_data.iloc[0]
            other_dances = [state_data.iloc[i] for i in range(1, len(state_data))] if len(state_data) > 1 else []
    else:
        # Default logic for other states
        for idx, dance_info in state_data.iterrows():
            if pd.notna(dance_info['DESCRIPTION']) and len(dance_info['DESCRIPTION']) > 100:
                if main_dance is None:
                    main_dance = dance_info
                else:
                    other_dances.append(dance_info)
            else:
                other_dances.append(dance_info)

        # If no detailed description found, use the first dance as main
        if main_dance is None:
            main_dance = state_data.iloc[0]
            other_dances = [state_data.iloc[i] for i in range(1, len(state_data))] if len(state_data) > 1 else []

    # Main featured dance card
    st.markdown(f"""
    <div class="dance-main-card">
        <h2 style="color: black; font-family: 'Playfair Display', serif; font-size: 2rem; text-align: center; margin-bottom: 1rem;">🎭 {selected_state} Dance Traditions</h2>
        <p style="color: #333; font-size: 1.1rem; margin-bottom: 2rem; text-align: center;">
            Discover the rich dance heritage of {selected_state}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Center the main dance image and info
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Display main dance name
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 1rem;">
            <h3 style="color: black; font-family: 'Playfair Display', serif; font-size: 1.8rem; margin-bottom: 0.5rem;">
                {main_dance['FOLK_DANCE']}
            </h3>
            <p style="color: #666; font-style: italic;">Featured Dance of {selected_state}</p>
        </div>
        """, unsafe_allow_html=True)

        # Display main dance image using cached loading
        img_path = f"Images/dance_photos/{main_dance['DOWNLOADED_DANCE_IMAGES']}"
        if pd.notna(main_dance['DOWNLOADED_DANCE_IMAGES']):
            img = load_and_cache_dance_image(img_path)
            if img:
                try:
                    # Create a copy for thumbnail to avoid modifying cached image
                    img_copy = img.copy()
                    img_copy.thumbnail((400, 350), Image.Resampling.LANCZOS)
                    st.image(img_copy, caption=main_dance['FOLK_DANCE'], use_container_width=True)
                except Exception as e:
                    st.error(f"Error processing image: {e}")
                    show_dance_placeholder()
            else:
                show_dance_placeholder()
        else:
            show_dance_placeholder()

    # Display main dance description if available
    if pd.notna(main_dance['DESCRIPTION']) and len(main_dance['DESCRIPTION']) > 50:
        st.markdown(f"""
        <div class="dance-main-description">
            <h3>About {main_dance['FOLK_DANCE']}</h3>
            <p>{main_dance['DESCRIPTION']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Display other dances from the state
    if other_dances:
        st.markdown('<h3 style="color: white; text-align: center; margin: 2rem 0;">Other Dance Forms of the State</h3>', unsafe_allow_html=True)

        # Display other dances in a grid with better alignment
        cols = st.columns(2)
        for i, dance_info in enumerate(other_dances):
            with cols[i % 2]:
                # Shorten dance name if too long and add state info
                dance_name = dance_info['FOLK_DANCE']
                if len(dance_name) > 15:
                    dance_name = dance_name[:15] + "..."

                st.markdown(f"""
                <div class="dance-description-card">
                    <h4 class="dance-description-title" style="color: #008080;">{dance_name} - {selected_state}</h4>
                    <p class="dance-description-text">
                        {dance_info['DESCRIPTION'][:150] + '...' if pd.notna(dance_info['DESCRIPTION']) and len(dance_info['DESCRIPTION']) > 150 else dance_info['DESCRIPTION'] if pd.notna(dance_info['DESCRIPTION']) else 'A traditional dance form from ' + selected_state}
                    </p>
                </div>
                """, unsafe_allow_html=True)

def show_dance_placeholder():
    """Show a placeholder for dance images"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #008080, #20B2AA);
               height: 350px; border-radius: 15px; display: flex;
               align-items: center; justify-content: center;
               font-size: 4rem; margin: 1rem 0; color: white;
               box-shadow: 0 10px 30px rgba(0,128,128,0.3);">
        💃
    </div>
    """, unsafe_allow_html=True)
