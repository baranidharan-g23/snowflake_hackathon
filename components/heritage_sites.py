import streamlit as st
import pandas as pd
import os
from PIL import Image
import random

@st.cache_data
def load_and_cache_image(image_path):
    """Load and cache image to avoid repeated file system calls"""
    if os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            return image
        except Exception as e:
            st.error(f"Error loading image {image_path}: {e}")
            return None
    return None

@st.cache_data
def get_image_info(image_path):
    """Cache image existence and dimensions"""
    if os.path.exists(image_path):
        try:
            with Image.open(image_path) as img:
                return {"exists": True, "size": img.size}
        except:
            return {"exists": False, "size": None}
    return {"exists": False, "size": None}

def load_heritage_data():
    """Load heritage sites data from CSV files"""
    try:
        # Load heritage sites data
        heritage_df = pd.read_csv('Datasets/heritage_sites.csv')

        # Load centrally protected monuments data (if exists)
        try:
            protected_df = pd.read_csv('Datasets/Centrally_Protected_Monuments_Domestic_Visits_2019_2024.csv')
        except:
            protected_df = pd.DataFrame()

        return heritage_df, protected_df
    except Exception as e:
        st.error(f"Error loading heritage data: {e}")
        return pd.DataFrame(), pd.DataFrame()

def show_heritage_section(heritage_sites_df=None, unesco_df=None):
    """Display enhanced heritage sites information with real data and creative storytelling"""
    st.markdown('<h2 class="section-header">🏛️ Heritage Sites</h2>', unsafe_allow_html=True)

    # Load heritage data
    heritage_df, protected_df = load_heritage_data()

    # Heritage sites overview with improved storytelling
    st.markdown("""
    <div style="background: rgba(255,255,255,0.98); backdrop-filter: blur(15px);
                padding: 3rem; border-radius: 20px; margin: 2rem 0;
                box-shadow: 0 15px 35px rgba(0,128,128,0.2); border: 3px solid #008080;">
        <h3 style="color: #008080; margin-bottom: 2rem; text-align: center;
                   font-family: 'Playfair Display', serif; font-size: 2.5rem; font-weight: 700;">
            🏛️ Chronicles of India's Living Heritage
        </h3>
        <p style="text-align: center; color: #333; font-size: 1.3rem; line-height: 1.8;
                  font-family: 'Poppins', sans-serif; margin-bottom: 1.5rem;">
            Journey through millennia of architectural marvels, sacred temples, royal palaces, and ancient monuments
            that tell the extraordinary story of India's cultural evolution across civilizations.
        </p>
        <p style="text-align: center; color: #666; font-size: 1.1rem; line-height: 1.6;
                  font-family: 'Poppins', sans-serif; margin-bottom: 0;">
            From the mystical caves of Ajanta to the eternal beauty of the Taj Mahal, each heritage site is a
            chapter in humanity's greatest architectural anthology.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Comprehensive Heritage Statistics with Storytelling
    if not heritage_df.empty:
        # Calculate comprehensive statistics
        total_sites = len(heritage_df)
        unique_states = heritage_df['STATE_NAME'].nunique()
        unique_cities = heritage_df['CITY_NAME'].nunique()
        heritage_types = heritage_df['HERITAGE_TYPE'].value_counts()

        # Calculate additional insights
        temple_count = len(heritage_df[heritage_df['HERITAGE_TYPE'].str.contains('Temple|temple', case=False, na=False)])
        monument_count = len(heritage_df[heritage_df['HERITAGE_TYPE'].str.contains('Monument|monument', case=False, na=False)])
        palace_count = len(heritage_df[heritage_df['HERITAGE_TYPE'].str.contains('Palace|palace', case=False, na=False)])

        # Top states by heritage count
        top_states = heritage_df['STATE_NAME'].value_counts().head(3)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                        padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                        margin-bottom: 1rem; text-align: center; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                        border: 2px solid #20B2AA; transition: transform 0.3s ease;">
                <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                           font-family: 'Poppins', sans-serif;">🏛️ Heritage Treasures</h5>
                <p style="margin: 0; line-height: 1.6; font-size: 2.5rem; color: #008080;
                          font-weight: bold; font-family: 'Poppins', sans-serif;">{total_sites}</p>
                <p style="margin: 0; color: #333; font-size: 1rem; font-weight: 500;">Documented Sites</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                        padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                        margin-bottom: 1rem; text-align: center; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                        border: 2px solid #20B2AA; transition: transform 0.3s ease;">
                <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                           font-family: 'Poppins', sans-serif;">🗺️ Cultural Regions</h5>
                <p style="margin: 0; line-height: 1.6; font-size: 2.5rem; color: #008080;
                          font-weight: bold; font-family: 'Poppins', sans-serif;">{unique_states}</p>
                <p style="margin: 0; color: #333; font-size: 1rem; font-weight: 500;">States & Territories</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                        padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                        margin-bottom: 1rem; text-align: center; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                        border: 2px solid #20B2AA; transition: transform 0.3s ease;">
                <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                           font-family: 'Poppins', sans-serif;">🏙️ Heritage Cities</h5>
                <p style="margin: 0; line-height: 1.6; font-size: 2.5rem; color: #008080;
                          font-weight: bold; font-family: 'Poppins', sans-serif;">{unique_cities}</p>
                <p style="margin: 0; color: #333; font-size: 1rem; font-weight: 500;">Historic Centers</p>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                        padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                        margin-bottom: 1rem; text-align: center; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                        border: 2px solid #20B2AA; transition: transform 0.3s ease;">
                <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                           font-family: 'Poppins', sans-serif;">🕉️ Sacred Temples</h5>
                <p style="margin: 0; line-height: 1.6; font-size: 2.5rem; color: #008080;
                          font-weight: bold; font-family: 'Poppins', sans-serif;">{temple_count}</p>
                <p style="margin: 0; color: #333; font-size: 1rem; font-weight: 500;">Divine Architecture</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        # Fallback statistics if data loading fails
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                        padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                        margin-bottom: 1rem; text-align: center; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                        border: 2px solid #20B2AA; transition: transform 0.3s ease;">
                <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                           font-family: 'Poppins', sans-serif;">🏰 Cultural Sites</h5>
                <p style="margin: 0; line-height: 1.6; font-size: 2.5rem; color: #008080;
                          font-weight: bold; font-family: 'Poppins', sans-serif;">32+</p>
                <p style="margin: 0; color: #333; font-size: 1rem; font-weight: 500;">UNESCO Sites</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                        padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                        margin-bottom: 1rem; text-align: center; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                        border: 2px solid #20B2AA; transition: transform 0.3s ease;">
                <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                           font-family: 'Poppins', sans-serif;">🌿 Natural Sites</h5>
                <p style="margin: 0; line-height: 1.6; font-size: 2.5rem; color: #008080;
                          font-weight: bold; font-family: 'Poppins', sans-serif;">7+</p>
                <p style="margin: 0; color: #333; font-size: 1rem; font-weight: 500;">UNESCO Sites</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                        padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                        margin-bottom: 1rem; text-align: center; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                        border: 2px solid #20B2AA; transition: transform 0.3s ease;">
                <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                           font-family: 'Poppins', sans-serif;">🏛️ Mixed Sites</h5>
                <p style="margin: 0; line-height: 1.6; font-size: 2.5rem; color: #008080;
                          font-weight: bold; font-family: 'Poppins', sans-serif;">1+</p>
                <p style="margin: 0; color: #333; font-size: 1rem; font-weight: 500;">UNESCO Sites</p>
            </div>
            """, unsafe_allow_html=True)

    # Interactive Heritage Slideshow
    show_heritage_slideshow()

    # Heritage Information Section
    show_heritage_information()

    # Regional Heritage Insights
    if not heritage_df.empty:
        show_regional_heritage_insights(heritage_df)

    # Dynamic Heritage Gallery
    if not heritage_df.empty:
        show_heritage_gallery(heritage_df)



    # Enhanced Heritage preservation message
    st.markdown("""
    <div style="background: rgba(255,255,255,0.98); backdrop-filter: blur(15px);
                padding: 3rem; border-radius: 20px; margin-top: 3rem; text-align: center;
                box-shadow: 0 15px 35px rgba(0,128,128,0.2); border: 3px solid #008080;
                border-left: 6px solid #20B2AA;">
        <h3 style="color: #008080; margin-bottom: 2rem; font-family: 'Playfair Display', serif;
                   font-size: 2.2rem; font-weight: 700;">
            🛡️ Preserving Our Heritage for Tomorrow
        </h3>
        <p style="font-size: 1.2rem; margin-bottom: 1.5rem; color: #333; line-height: 1.7;
                  font-family: 'Poppins', sans-serif;">
            India's heritage sites are not just monuments of the past, but living testimonies of our rich cultural legacy.
            Each site tells a unique story of artistic achievement, spiritual devotion, and historical significance that
            connects us to our ancestors and guides us toward the future.
        </p>
        <p style="font-size: 1.1rem; color: #666; line-height: 1.6; font-family: 'Poppins', sans-serif;">
            Through dedicated conservation efforts, scientific preservation techniques, community involvement, and
            responsible tourism, we ensure these irreplaceable treasures remain intact for future generations to
            experience, learn from, and cherish as symbols of human creativity and cultural diversity.
        </p>
        <div style="margin-top: 2rem; padding: 1.5rem; background: rgba(0,128,128,0.05);
                    border-radius: 15px; border: 2px solid #20B2AA;">
            <p style="color: #008080; font-size: 1rem; margin: 0; font-weight: 600;
                      font-family: 'Poppins', sans-serif;">
                🌍 "Heritage is our legacy from the past, what we live with today, and what we pass on to future generations." - UNESCO
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_heritage_slideshow():
    """Display an interactive heritage slideshow with real images"""
    st.markdown("""
    <div style="text-align: center;">
        <br>
        <h3 style="color: white; text-align: center; margin: 3rem 0 2rem 0; font-family: 'Playfair Display', serif;
               font-size: 3.5rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.5); font-weight: 700;">
            🌟 Heritage Highlights
        </h3>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced featured heritage sites with more diverse examples
    featured_sites = [
        {
            "name": "Taj Mahal",
            "location": "Agra, Uttar Pradesh",
            "image": "Images/heritage_images/Agra_TAJ_MAHAL.jpg",
            "description": "The eternal symbol of love, this ivory-white marble mausoleum stands as a testament to Mughal architectural brilliance and eternal devotion. Built by Shah Jahan for his beloved wife Mumtaz Mahal.",
            "significance": "UNESCO World Heritage Site & New Seven Wonders of the World"
        },
        {
            "name": "Red Fort",
            "location": "Agra, Uttar Pradesh",
            "image": "Images/heritage_images/Agra_RED_FORT.jpg",
            "description": "The majestic fortress palace of the Mughal emperors, where India's independence was proclaimed and history was written in red sandstone. A symbol of Mughal power and architectural mastery.",
            "significance": "Symbol of India's sovereignty and Mughal architectural heritage"
        },
        {
            "name": "Gwalior Fort",
            "location": "Madhya Pradesh",
            "image": "Images/heritage_images/Gwalior_Gwalior_Fort.jpg",
            "description": "The 'Pearl among fortresses in Hind', this hilltop citadel has witnessed the rise and fall of dynasties across a millennium of Indian history. Known for its impregnable defenses and musical heritage.",
            "significance": "One of India's most magnificent forts with rich cultural legacy"
        },
        {
            "name": "Brihadeeswarar Temple",
            "location": "Thanjavur, Tamil Nadu",
            "image": "Images/heritage_images/Thanjavur_Bragadeeswarar_Temple.jpg",
            "description": "A thousand-year-old architectural marvel dedicated to Lord Shiva, showcasing the pinnacle of Chola dynasty's artistic and engineering prowess. The temple's towering vimana is a masterpiece of Dravidian architecture.",
            "significance": "UNESCO World Heritage Site and masterpiece of Dravidian architecture"
        },
        {
            "name": "Shaniwarwada Palace",
            "location": "Pune, Maharashtra",
            "image": "Images/heritage_images/Pune_City_Shaniwarwada.jpg",
            "description": "The historic fortified palace of the Peshwas of the Maratha Empire, representing the zenith of Maratha architecture and political power in the 18th century.",
            "significance": "Symbol of Maratha empire and architectural heritage"
        },
        {
            "name": "Fatehpur Sikri",
            "location": "Agra, Uttar Pradesh",
            "image": "Images/heritage_images/Agra_FATEHPURI_SIKRI.jpg",
            "description": "Emperor Akbar's magnificent capital city, a perfect blend of Hindu and Islamic architectural styles. This ghost city tells the story of Mughal grandeur and religious tolerance.",
            "significance": "UNESCO World Heritage Site and architectural fusion masterpiece"
        },
        {
            "name": "Ujjayanta Palace",
            "location": "Agartala, Tripura",
            "image": "Images/heritage_images/Agartala_Ujjayanta_Palace.jpg",
            "description": "The former royal palace of the Kingdom of Tripura, showcasing Indo-Saracenic architecture with beautiful gardens and intricate design elements reflecting royal grandeur.",
            "significance": "Symbol of Tripura's royal heritage and architectural elegance"
        },
        {
            "name": "Akbar's Tomb",
            "location": "Agra, Uttar Pradesh",
            "image": "Images/heritage_images/Agra_AKBARS_TOMB.jpg",
            "description": "The magnificent mausoleum of Emperor Akbar the Great, representing the synthesis of Hindu, Christian, Islamic and Buddhist themes reflecting Akbar's secular philosophy.",
            "significance": "Architectural testament to Akbar's religious tolerance and Mughal grandeur"
        }
    ]

    # Initialize slideshow state
    if 'heritage_slide_index' not in st.session_state:
        st.session_state.heritage_slide_index = 0

    # Navigation buttons
    col1, col2, col3 = st.columns([1, 7, 1])

    with col1:
        if st.button("◀ Previous", key="heritage_prev"):
            st.session_state.heritage_slide_index = (st.session_state.heritage_slide_index - 1) % len(featured_sites)

    with col3:
        if st.button("Next ▶", key="heritage_next"):
            st.session_state.heritage_slide_index = (st.session_state.heritage_slide_index + 1) % len(featured_sites)

    # Display current slide
    current_site = featured_sites[st.session_state.heritage_slide_index]

    # Create slideshow display
    col1, col2 = st.columns([1, 1])

    with col1:
        # Use cached image loading
        image = load_and_cache_image(current_site["image"])
        if image:
            st.image(image, use_container_width=True, caption=f"{current_site['name']}, {current_site['location']}")
        else:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #008080, #20B2AA); color: white;
                        padding: 8rem 2rem; border-radius: 15px; text-align: center; margin: 1rem 0;">
                <h2 style="color: white; margin-bottom: 1rem; font-size: 2rem;">🏛️</h2>
                <h3 style="color: white; margin: 0; font-size: 1.5rem;">{current_site['name']}</h3>
                <p style="color: rgba(255,255,255,0.8); margin: 0.5rem 0 0 0;">{current_site['location']}</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.98); backdrop-filter: blur(15px);
                    padding: 2rem; border-radius: 20px; height: 100%;
                    box-shadow: 0 15px 35px rgba(0,128,128,0.2); border: 3px solid #008080;">
            <h3 style="color: #008080; margin-bottom: 1rem; font-family: 'Playfair Display', serif;
                       font-size: 1.8rem; font-weight: 700;">
                {current_site['name']}
            </h3>
            <p style="color: #666; font-size: 1rem; margin-bottom: 1rem; font-family: 'Poppins', sans-serif;">
                📍 {current_site['location']}
            </p>
            <p style="color: #333; font-size: 1rem; line-height: 1.7; margin-bottom: 1.5rem;
                      font-family: 'Poppins', sans-serif; text-align: justify;">
                {current_site['description']}
            </p>
            <div style="border-top: 2px solid #e0e0e0; padding-top: 1rem;">
                <p style="color: #008080; font-size: 0.9rem; font-weight: 600; margin: 0;
                          font-family: 'Poppins', sans-serif;">
                    ✨ {current_site['significance']}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Slide indicators with enhanced styling
    st.markdown(f"""
    <div style="text-align: center; margin: 1.5rem 0;">
        <p style="color: white; font-size: 1.1rem; font-family: 'Poppins', sans-serif;
                  text-shadow: 2px 2px 4px rgba(0,0,0,0.5); font-weight: 600;">
            {st.session_state.heritage_slide_index + 1} of {len(featured_sites)} Heritage Treasures
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_heritage_information():
    """Display general information about Indian Heritage similar to dance info section"""
    st.markdown("""
    <h3 style="color: white; text-align: center; margin: 3rem 0 2rem 0; font-family: 'Playfair Display', serif;
               font-size: 2.3rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.5); font-weight: 700;">
        🏛️ Guardians of India's Timeless Legacy
    </h3>
    """, unsafe_allow_html=True)

    # Create columns for heritage information
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA;">
            <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                       font-family: 'Poppins', sans-serif;">🏛️ Cultural Heritage</h5>
            <p style="margin: 0; line-height: 1.7; color: #333; font-family: 'Poppins', sans-serif;">
                India's cultural heritage sites represent over 5,000 years of continuous civilization.
                From ancient rock-cut caves to magnificent Mughal architecture, these monuments showcase
                the artistic genius, spiritual devotion, and architectural innovations of various dynasties
                and cultures that flourished on Indian soil.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA;">
            <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                       font-family: 'Poppins', sans-serif;">🎨 Artistic Excellence</h5>
            <p style="margin: 0; line-height: 1.7; color: #333; font-family: 'Poppins', sans-serif;">
                Each heritage site tells a unique story through intricate carvings, magnificent frescoes,
                and architectural marvels. From the delicate inlay work of the Taj Mahal to the elaborate
                sculptures of Khajuraho, these sites represent the pinnacle of Indian artistic achievement
                across different periods and regions.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA;">
            <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                       font-family: 'Poppins', sans-serif;">🌿 Natural Wonders</h5>
            <p style="margin: 0; line-height: 1.7; color: #333; font-family: 'Poppins', sans-serif;">
                India's natural heritage sites protect unique ecosystems and biodiversity hotspots.
                From the mangrove forests of Sundarbans to the Western Ghats, these sites preserve
                critical habitats for endangered species and maintain ecological balance essential
                for environmental sustainability.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA;">
            <h5 style="color: #008080; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;
                       font-family: 'Poppins', sans-serif;">🛡️ Conservation Legacy</h5>
            <p style="margin: 0; line-height: 1.7; color: #333; font-family: 'Poppins', sans-serif;">
                UNESCO recognition brings global attention to conservation efforts, ensuring these
                irreplaceable treasures are preserved for future generations. Through scientific
                conservation, community involvement, and sustainable tourism, India continues to
                protect its heritage while sharing it with the world.
            </p>
        </div>
        """, unsafe_allow_html=True)

def display_heritage_site_card(site):
    """Display an enhanced heritage site card with better styling"""
    # Determine icon based on type
    type_icon = "🏰" if site["type"] == "Cultural" else "🌿" if site["type"] == "Natural" else "🏛️"

    # Get features if available
    features = site.get('features', '')

    st.markdown(f"""
    <div style="background: rgba(255,255,255,0.98); backdrop-filter: blur(15px);
                padding: 2rem; border-radius: 20px; margin: 1.5rem 0;
                box-shadow: 0 15px 35px rgba(0,128,128,0.2); border: 3px solid #008080;
                transition: transform 0.3s ease, box-shadow 0.3s ease; min-height: 400px;
                border-left: 6px solid #20B2AA;">
        <div style="text-align: center; margin-bottom: 1.5rem;">
            <h4 style="color: #008080; margin-bottom: 0.8rem; font-size: 1.5rem; font-weight: 700;
                       font-family: 'Playfair Display', serif;">
                {type_icon} {site['name']}
            </h4>
            <p style="color: #666; font-size: 1rem; margin-bottom: 0.8rem; font-family: 'Poppins', sans-serif;">
                📍 {site['location']} | 🗓️ UNESCO {site['year']}
            </p>
            <span style="background: linear-gradient(135deg, #008080, #20B2AA); color: white;
                         padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.9rem;
                         font-weight: 600; font-family: 'Poppins', sans-serif;">
                {site['type']} Heritage
            </span>
        </div>

        <div style="margin-bottom: 1.5rem;">
            <p style="color: #333; font-size: 1rem; line-height: 1.7; text-align: justify;
                      font-family: 'Poppins', sans-serif;">
                {site['description'][:200]}{'...' if len(site['description']) > 200 else ''}
            </p>
        </div>

        {f'''<div style="margin-bottom: 1.5rem; background: rgba(0,128,128,0.05);
                        padding: 1rem; border-radius: 10px; border-left: 4px solid #20B2AA;">
            <h6 style="color: #008080; margin-bottom: 0.5rem; font-size: 0.9rem; font-weight: 600;
                       font-family: 'Poppins', sans-serif;">🎯 Key Features:</h6>
            <p style="color: #333; font-size: 0.9rem; margin: 0; font-family: 'Poppins', sans-serif;">
                {features}
            </p>
        </div>''' if features else ''}

        <div style="border-top: 2px solid #e0e0e0; padding-top: 1rem;">
            <p style="color: #008080; font-size: 0.95rem; font-weight: 600; margin: 0;
                      font-family: 'Poppins', sans-serif; line-height: 1.5;">
                ✨ {site['significance']}
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_heritage_gallery(heritage_df):
    """Display a dynamic gallery of heritage sites from CSV data with enhanced storytelling"""
    if heritage_df.empty:
        return

    st.markdown("""
    <h3 style="color: white; text-align: center; margin: 3rem 0 2rem 0; font-family: 'Playfair Display', serif;
               font-size: 2.5rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.5); font-weight: 700;">
        🎨 Interactive Heritage Gallery
    </h3>
    """, unsafe_allow_html=True)

    # Gallery introduction with properly sized white box
    st.markdown("""
    <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                padding: 2rem; border-radius: 15px; margin: 1.5rem 0;
                box-shadow: 0 8px 25px rgba(0,128,128,0.15); border: 2px solid #20B2AA;
                text-align: center; border-left: 6px solid #008080;">
        <p style="color: #333; font-size: 1.2rem; line-height: 1.6; margin: 0;
                  font-family: 'Poppins', sans-serif; font-weight: 500;">
            🔍 Explore India's documented heritage treasures through our interactive gallery.
            Filter by region, heritage type, or city to discover the architectural marvels that define our cultural landscape.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Filter options
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_state = st.selectbox(
            "🗺️ Select State",
            ["All States"] + sorted(heritage_df['STATE_NAME'].unique().tolist()),
            key="heritage_state_filter"
        )

    with col2:
        heritage_types = heritage_df['HERITAGE_TYPE'].unique().tolist()
        selected_type = st.selectbox(
            "🏛️ Heritage Type",
            ["All Types"] + sorted([t for t in heritage_types if pd.notna(t)]),
            key="heritage_type_filter"
        )

    with col3:
        cities = heritage_df['CITY_NAME'].unique().tolist() if selected_state == "All States" else heritage_df[heritage_df['STATE_NAME'] == selected_state]['CITY_NAME'].unique().tolist()
        selected_city = st.selectbox(
            "🏙️ Select City",
            ["All Cities"] + sorted([c for c in cities if pd.notna(c)]),
            key="heritage_city_filter"
        )

    # Filter data based on selections
    filtered_df = heritage_df.copy()

    if selected_state != "All States":
        filtered_df = filtered_df[filtered_df['STATE_NAME'] == selected_state]

    if selected_type != "All Types":
        filtered_df = filtered_df[filtered_df['HERITAGE_TYPE'] == selected_type]

    if selected_city != "All Cities":
        filtered_df = filtered_df[filtered_df['CITY_NAME'] == selected_city]

    # Display filtered results
    if not filtered_df.empty:
        # Results summary with properly sized white box
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; margin: 1.5rem 0;
                    box-shadow: 0 8px 25px rgba(0,128,128,0.15); border: 2px solid #20B2AA;
                    text-align: center; border-left: 6px solid #008080;">
            <h5 style="color: #008080; margin-bottom: 1rem; font-family: 'Playfair Display', serif;
                       font-size: 1.5rem; font-weight: 700;">
                🎯 Discovered {len(filtered_df)} Heritage Treasures
            </h5>
            <p style="color: #666; margin: 0; font-family: 'Poppins', sans-serif; font-size: 1.1rem; line-height: 1.5;">
                Each site tells a unique story of India's rich cultural tapestry and architectural evolution
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Create a compact gallery layout without gaps
        total_sites = len(filtered_df)
        sites_list = list(filtered_df.iterrows())

        # Display all sites at once
        sites_to_show = sites_list

        # Add custom CSS for better styling
        st.markdown("""
        <style>
        .heritage-card-container {
            margin-bottom: 0 !important;
        }

        .heritage-card-container > div {
            margin-bottom: 0 !important;
        }

        /* Remove default Streamlit spacing */
        .element-container {
            margin-bottom: 0 !important;
        }

        /* Ensure consistent column heights */
        .stColumn > div {
            height: 100%;
        }
        </style>
        """, unsafe_allow_html=True)

        # Group images by dimensions for better layout (now using cached function)

        def categorize_by_aspect_ratio(width, height):
            """Categorize images by aspect ratio"""
            if width is None or height is None:
                return "placeholder"

            aspect_ratio = width / height
            if aspect_ratio > 1.5:
                return "landscape"  # Wide images
            elif aspect_ratio < 0.75:
                return "portrait"   # Tall images
            else:
                return "square"     # Square-ish images

        # Group sites by image dimensions
        grouped_sites = {"landscape": [], "square": [], "portrait": [], "placeholder": []}

        for _, site in sites_to_show:
            image_path = f"Images/heritage_images/{site['IMAGE_NAME']}"
            image_info = get_image_info(image_path)  # Use cached function
            if image_info["exists"] and image_info["size"]:
                category = categorize_by_aspect_ratio(image_info["size"][0], image_info["size"][1])
            else:
                category = "placeholder"
            grouped_sites[category].append((_, site))

        # Display groups in order: landscape, square, portrait, placeholder
        for group_name in ["landscape", "square", "portrait", "placeholder"]:
            group_sites = grouped_sites[group_name]
            if not group_sites:
                continue

            # Determine columns per row based on image type
            if group_name == "landscape":
                cols_per_row = 2  # Fewer columns for wide images
            elif group_name == "portrait":
                cols_per_row = 4  # More columns for tall images
            else:
                cols_per_row = 3  # Standard for square and placeholder

            # Display sites in this group
            for i in range(0, len(group_sites), cols_per_row):
                cols = st.columns(cols_per_row, gap="small")

                for j in range(cols_per_row):
                    if i + j < len(group_sites):
                        _, site = group_sites[i + j]

                        with cols[j]:
                            # Create a styled container for each heritage site
                            st.markdown(f"""
                            <div style="background: white; backdrop-filter: blur(10px);
                                        border-radius: 15px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                                        border: 2px solid #20B2AA; margin-bottom: 1rem; height: 100%;
                                        transition: transform 0.3s ease;">
                            """, unsafe_allow_html=True)

                            # Display image using cached loading
                            image_path = f"Images/heritage_images/{site['IMAGE_NAME']}"
                            image = load_and_cache_image(image_path)
                            if image:
                                st.image(image, use_container_width=True, caption="")
                            else:
                                st.markdown("""
                                <div style="width: 100%; height: 200px; background: linear-gradient(135deg, #008080, #20B2AA);
                                            display: flex; align-items: center; justify-content: center; color: white;
                                            font-size: 1rem; font-family: 'Poppins', sans-serif;">
                                    🏛️<br>Image Coming Soon
                                </div>
                                """, unsafe_allow_html=True)

                            # Display content
                            st.markdown(f"""
                            <div style="padding: 1.5rem;">
                                <div style="color: white; font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem;
                                            font-family: 'Playfair Display', serif; line-height: 1.3;">
                                    {site['HERITAGE_NAME']}
                                </div>
                                <div style="color: white; font-size: 0.9rem; margin-bottom: 0.8rem;
                                            font-family: 'Poppins', sans-serif;">
                                    📍 {site['CITY_NAME']}, {site['STATE_NAME']}
                                </div>
                                <div style="background: linear-gradient(135deg, #008080, #20B2AA); color: white;
                                            padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem;
                                            font-weight: 600; display: inline-block; font-family: 'Poppins', sans-serif;">
                                    {site['HERITAGE_TYPE']}
                                </div>
                            </div>
                            """, unsafe_allow_html=True)

                            st.markdown("</div>", unsafe_allow_html=True)

        # Display summary
        st.success(f"Displaying all {total_sites} heritage sites")
    else:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 3rem; border-radius: 15px; margin: 2rem 0;
                    box-shadow: 0 8px 25px rgba(0,128,128,0.15); border: 2px solid #20B2AA;
                    text-align: center;">
            <h5 style="color: #008080; margin-bottom: 1.5rem; font-family: 'Poppins', sans-serif; font-size: 1.4rem;">
                🔍 No Heritage Sites Found
            </h5>
            <p style="color: #666; margin-bottom: 1rem; font-family: 'Poppins', sans-serif; font-size: 1.1rem;">
                Try adjusting your filters to explore more heritage treasures across India
            </p>
            <p style="color: #999; margin: 0; font-family: 'Poppins', sans-serif; font-size: 0.9rem;">
                💡 Tip: Start with "All States" or "All Types" to see the full collection
            </p>
        </div>
        """, unsafe_allow_html=True)

# Note: display_heritage_gallery_card function removed - now using CSS Grid approach

def show_regional_heritage_insights(heritage_df):
    """Display regional heritage insights and patterns"""
    st.markdown("""
    <h3 style="color: white; text-align: center; margin: 3rem 0 2rem 0; font-family: 'Playfair Display', serif;
               font-size: 2.3rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.5); font-weight: 700;">
        🗺️ Regional Heritage Chronicles
    </h3>
    """, unsafe_allow_html=True)

    # Calculate regional statistics
    state_counts = heritage_df['STATE_NAME'].value_counts().head(5)
    heritage_type_counts = heritage_df['HERITAGE_TYPE'].value_counts().head(6)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA;">
            <h5 style="color: #008080; margin-bottom: 1.5rem; font-size: 1.4rem; font-weight: 600;
                       font-family: 'Poppins', sans-serif; text-align: center;">🏆 Heritage Powerhouses</h5>
        </div>
        """, unsafe_allow_html=True)

        for i, (state, count) in enumerate(state_counts.items()):
            rank_emoji = ["🥇", "🥈", "🥉", "🏅", "⭐"][i]
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px;
                        margin-bottom: 0.5rem; border-left: 4px solid #20B2AA;">
                <p style="margin: 0; color: #333; font-family: 'Poppins', sans-serif;">
                    {rank_emoji} <strong>{state}</strong>: {count} heritage sites
                </p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px);
                    padding: 2rem; border-radius: 15px; border-left: 6px solid #008080;
                    margin-bottom: 1rem; box-shadow: 0 8px 25px rgba(0,128,128,0.15);
                    border: 2px solid #20B2AA;">
            <h5 style="color: #008080; margin-bottom: 1.5rem; font-size: 1.4rem; font-weight: 600;
                       font-family: 'Poppins', sans-serif; text-align: center;">🏛️ Heritage Categories</h5>
        </div>
        """, unsafe_allow_html=True)

        type_emojis = {"Temple": "🕉️", "Monument": "🏛️", "Palace": "👑", "Fort": "🏰", "Church": "⛪", "Mosque": "🕌"}

        for heritage_type, count in heritage_type_counts.items():
            emoji = type_emojis.get(heritage_type, "🏛️")
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px;
                        margin-bottom: 0.5rem; border-left: 4px solid #20B2AA;">
                <p style="margin: 0; color: #333; font-family: 'Poppins', sans-serif;">
                    {emoji} <strong>{heritage_type}</strong>: {count} sites
                </p>
            </div>
            """, unsafe_allow_html=True)

    # Heritage storytelling insights
    st.markdown("""
    <div style="background: rgba(255,255,255,0.98); backdrop-filter: blur(15px);
                padding: 2.5rem; border-radius: 20px; margin: 2rem 0;
                box-shadow: 0 15px 35px rgba(0,128,128,0.2); border: 3px solid #008080;">
        <h4 style="color: #008080; margin-bottom: 1.5rem; text-align: center;
                   font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 700;">
            📖 Stories Written in Stone and Time
        </h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem;">
            <div>
                <h6 style="color: #008080; margin-bottom: 1rem; font-size: 1.1rem; font-weight: 600;">
                    🏛️ Architectural Evolution
                </h6>
                <p style="color: #333; font-size: 1rem; line-height: 1.7; margin: 0;">
                    From ancient rock-cut caves to Mughal masterpieces, India's heritage sites chronicle
                    the evolution of architectural styles across millennia, each era leaving its distinctive mark.
                </p>
            </div>
            <div>
                <h6 style="color: #008080; margin-bottom: 1rem; font-size: 1.1rem; font-weight: 600;">
                    🌍 Cultural Confluence
                </h6>
                <p style="color: #333; font-size: 1rem; line-height: 1.7; margin: 0;">
                    These monuments stand as witnesses to India's role as a cultural crossroads, where
                    diverse traditions, religions, and artistic styles merged to create unique masterpieces.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
