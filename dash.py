import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set Seaborn theme for vibrant plots
sns.set(style="whitegrid", palette="muted", color_codes=True)

# Load the dataset
file_path = 'co2_mm_mlo.csv'  # Ensure the file is in the same directory
data = pd.read_csv(file_path, comment='#', skip_blank_lines=True)

# Create a Date column for plotting
data['Date'] = pd.to_datetime(data[['year', 'month']].assign(day=1))

# Set a background image (Earth in space)
page_bg_img = '''
<style>
body {
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/c/c1/Earth_from_Space_%282004%29.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: #FFFFFF;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Set the title of the app with a vibrant color
st.markdown("<h1 style='text-align: center; color: #00FFFF;'>The Story of CO2 and Our Changing Climate 🌎</h1>",
            unsafe_allow_html=True)

# Add a more creative narrative section with descriptive insights
st.markdown("""
### The Tale of Carbon and Climate 🌍
Since the dawn of the Industrial Revolution, humankind has made incredible advancements, but at what cost? 
The concentration of carbon dioxide (CO2) in our atmosphere has skyrocketed, acting as a blanket that traps heat and warms the planet.

The Mauna Loa Observatory, located in Hawaii, has been continuously monitoring atmospheric CO2 levels since 1958, providing invaluable data for understanding the trajectory of climate change.

In this dashboard, we explore the patterns of CO2 concentrations and how they reflect the health of our planet.
""")

# Add some vibrant colors to the plot with creative commentary
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data['Date'], data['average'], label='Average CO2 Concentration (ppm)', color='#00FF00', linewidth=2)
ax.axhline(y=350, color='#FF4500', linestyle='--', label='350 ppm (Safe Level)')
ax.axhline(y=400, color='#FFA500', linestyle='--', label='400 ppm (Critical Level)')

ax.set_xlabel('Year', fontsize=12, color='#00FFFF')
ax.set_ylabel('CO2 Concentration (ppm)', fontsize=12, color='#00FFFF')
ax.set_title('CO2 Concentrations Over Time (1958 - Present)', fontsize=16, color='#00FFFF')
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, which='both', linestyle='--', linewidth=0.7)

# Customize plot background for more futuristic appearance
ax.set_facecolor('#1c1c1c')
fig.patch.set_facecolor('#2F4F4F')

# Show the plot in Streamlit
st.pyplot(fig)

# Add another narrative with deeper insights and vibrant storytelling
st.markdown("""
### CO2: The Hidden Force of Climate Change 🔥
As CO2 levels steadily increase, so does the warming potential of Earth's atmosphere. 

- In 1960, the CO2 concentration hovered around 316 ppm. The planet was still within a relatively safe range.
- By 1990, global industrialization had pushed CO2 levels to over 350 ppm, surpassing what many scientists consider the 'safe' limit.
- In 2023, we reached a staggering 417 ppm, breaking records and signaling a planet under stress.

The numbers tell a story of transformation—one that’s urgent and ongoing. The effects are already visible: melting ice caps, rising sea levels, more extreme weather patterns. What comes next?
""")

# Comparative Analysis Section with vibrant visuals and futuristic style
st.markdown("<h3 style='color:#00FFFF;'>A Time-Lapse of CO2 Concentrations Over Decades</h3>", unsafe_allow_html=True)
st.write("""
Let’s compare the CO2 levels between two significant years of your choice, from the early days of measurements to recent years. How far have we come?
""")

year1 = st.sidebar.selectbox('Select a Year from the Past', data['year'].unique())
year2 = st.sidebar.selectbox('Select a Recent Year', data['year'].unique())

# Filter data for the selected years
filtered_data1 = data[data['year'] == year1]
filtered_data2 = data[data['year'] == year2]
# Create comparative plot with vibrant colors
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(filtered_data1['month'], filtered_data1['average'], label=f'CO2 in {year1}', color='#1E90FF', linewidth=2)
ax2.plot(filtered_data2['month'], filtered_data2['average'], label=f'CO2 in {year2}', color='#FF6347', linewidth=2)

ax2.set_xlabel('Month', fontsize=12, color='#00FFFF')
ax2.set_ylabel('CO2 Concentration (ppm)', fontsize=12, color='#00FFFF')
ax2.set_title(f'CO2 Concentrations: {year1} vs {year2}', fontsize=16, color='#00FFFF')
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, which='both', linestyle='--', linewidth=0.7)

# Customize plot background
ax2.set_facecolor('#1c1c1c')
fig2.patch.set_facecolor('#2F4F4F')

# Show the comparative plot in Streamlit
st.pyplot(fig2)

# Narrative for comparative analysis
st.markdown(f"In {year1}, the average CO2 concentration was {filtered_data1['average'].mean():.2f} ppm.")
st.markdown(f"In {year2}, the average CO2 concentration was {filtered_data2['average'].mean():.2f} ppm.")

# Add a call to action for the audience
st.markdown("""
### What Can We Do? 🤔
It’s not too late. The choices we make now—whether as individuals, corporations, or governments—will determine the future of our planet.

- Switch to renewable energy.
- Promote sustainable practices.
- Advocate for policies to reduce emissions.

The future of the planet is in our hands. Together, we can shape a better tomorrow 🌱.
""")

# Add footer with futuristic style
st.markdown("""
<hr>
<p style='text-align: center; color: #00FFFF;'>Powered by NOAA GML Data | Visualizing the Future of Our Planet 🌍</p>
""", unsafe_allow_html=True)