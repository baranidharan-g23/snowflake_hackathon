# Indian Cultural Heritage & Tourism Dashboard

A comprehensive Streamlit application showcasing India's rich cultural heritage through data-driven insights and promoting responsible tourism.

## Features

### 🏠 Homepage
- Overview of Indian cultural heritage
- Key tourism statistics and metrics
- Interactive navigation to different sections

### 🎭 Traditional Art Forms
- **Festivals**: State-wise festivals with seasonal information and images
- **Dance Forms**: Traditional and classical dance forms across India
- **Heritage Sites**: City-wise heritage monuments and archaeological sites

### 📊 Tourism Analytics
- **ITA Trends**: International Tourist Arrivals analysis (2001-2023)
- **Seasonal Patterns**: Month-wise tourism trends and seasonality
- **State-wise Analysis**: Regional tourism distribution and growth
- **Untouched Destinations**: Analysis of underexplored regions

### 🌍 Cultural Experiences
- **Cultural Calendar**: Month-wise festival exploration
- **Regional Diversity**: Cultural comparison across Indian regions

### ♻️ Responsible Tourism
- **Sustainability Guidelines**: Best practices for cultural tourism
- **Community Impact**: Understanding tourism's effect on local communities
- **Tourism Balance**: Analysis of tourism concentration and recommendations

## Data Sources

The application uses the following datasets:
- `Festivals.csv`: State-wise festival information with descriptions
- `dance_photos_csv.csv`: Traditional dance forms by state
- `ITAs(1-23).csv`: International Tourist Arrivals (2001-2023)
- `ITAs(21-23)_Month_wise.csv`: Monthly tourism data (2021-2023)
- `State_wise_tourist_2022_2023.csv`: State-wise tourism statistics

## Installation

1. Clone or download the repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Navigate to the project directory:
   ```bash
   cd dev/personal/Snowflake_frontend
   ```

2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

3. Open your browser and go to `http://localhost:8501`

## Project Structure

```
dev/personal/Snowflake_frontend/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                      # Project documentation
├── Festivals.csv                  # Festival data
├── dance_photos_csv.csv           # Dance forms data
├── ITAs(1-23).csv                # Tourism arrivals data
├── ITAs(21-23)_Month_wise.csv     # Monthly tourism data
├── State_wise_tourist_2022_2023.csv # State tourism data
├── Festivals_images/              # Festival images
├── dance_photos/                  # Dance form images
├── heritage_images/               # Heritage site images
└── monument_images/               # Monument images
```

## Key Insights

### Tourism Trends
- **Peak Recovery**: Tourism showed strong recovery in 2023 (18.9M arrivals)
- **Seasonal Patterns**: December and November are peak months
- **Regional Distribution**: North and South India dominate tourism

### Cultural Heritage
- **Festivals**: 80+ festivals across all states and seasons
- **Dance Forms**: 30+ traditional and classical dance forms
- **Heritage Sites**: Hundreds of archaeological and cultural monuments

### Untouched Destinations
- **Northeast India**: High cultural value but low tourism
- **Island Territories**: Unique ecosystems with limited visitors
- **Tribal Areas**: Rich traditions with sustainable tourism potential

## Responsible Tourism Focus

The application emphasizes:
- **Cultural Preservation**: Protecting traditions while promoting tourism
- **Community Benefits**: Ensuring local communities benefit from tourism
- **Sustainable Practices**: Promoting eco-friendly and responsible travel
- **Balanced Development**: Preventing over-tourism in popular destinations

## Technical Features

- **Interactive Visualizations**: Plotly charts and graphs
- **Image Galleries**: Cultural images with proper attribution
- **Data Analytics**: Statistical analysis of tourism trends
- **Responsive Design**: Mobile-friendly interface
- **Performance Optimization**: Cached data loading

## Future Enhancements

- Integration with live tourism APIs
- Machine learning predictions for tourism trends
- Interactive maps with geographic data
- User-generated content and reviews
- Multi-language support
- Mobile application development

## Contributing

This project showcases India's cultural heritage and promotes responsible tourism. Contributions for data updates, feature enhancements, and bug fixes are welcome.

## License

This project is for educational and cultural promotion purposes.
