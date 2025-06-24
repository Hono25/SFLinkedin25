import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import os
from PIL import Image
import os

# Set Streamlit page configuration

st.set_page_config(page_title="France Electricity Analysis", layout="wide")
st.title("French Electricity Consumption and Production : Potential Blackout Analysis")
st.sidebar.title("Table of contents")
pages=["Introduction","Exploration", "DataVizualization","Conclusion"]
page=st.sidebar.radio("Go to", pages)

# Path to your image
image_path = "pexels-barnabas-davoti-31615494-32253074.jpg"
st.sidebar.write("### Project Members")
st.sidebar.write("""- Ana Karina KAPITANY\n- Andrea GRANT\n- Honorine Mbabi Kesseng\n- Laetitia NIKUZE\n
                 \n Mentor: Christoph F and Support:Nicolas Fradin""")

from PIL import Image
image = Image.open("DataScientest_logo.jpg")
st.sidebar.image(image, caption="Datenscientest", width=100)

# Check if the image exists before displaying
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.sidebar.image(image, caption="DataScientest Mars 2025", use_container_width=True)
else:
    st.sidebar.error("Image not found.")

# File uploader
uploaded_file="eco.csv"
df= pd.read_csv(uploaded_file, sep=";")

if page == pages[0] : 
  
  image_path_e = "pexels-barnabas-davoti-31615494-32253074.jpg"
  st.write("Presented by: Ana, Andrea, Honorine and Laetitia")
  
  st.text("Introduction to Our Project: Renewable Energy and Blackouts/Potential Blackouts in France")
  st.text("Welcome to our project, where we delve into the dynamic landscape of renewable energy in France, with a specific focus on its relationship with grid stability and the risk of blackouts. As the world increasingly shifts towards sustainable practices, understanding the progress and potential of clean energy sources is more critical than ever. France, with its ambitious environmental goals and diverse energy portfolio, offers a fascinating case study in this global transition.")
  st.text("In this project, we aim to explore the various facets of renewable energy development within France. We will examine the current state of play, highlighting key technologies, policies, and the impact of these initiatives on the nation's energy independence and environmental footprint. Crucially, we will also investigate how the integration of renewable energy sources affects the reliability of the power grid, analyzing the challenges and solutions related to potential blackouts. Our goal is to provide a comprehensive overview that sheds light on both the achievements and the ongoing challenges in France's journey towards a greener and more secure energy future.")

if page == pages[1] : 
    uploaded_file = "eco.csv"
    @st.cache_data
    def load_data(file):
        df = pd.read_csv(file, sep=';')

        st.write("## Presentation of data")
        st.subheader("Raw Data Preview")
        st.dataframe(df.head())
        st.text("This is an analysis of the initial dataset. The original dataset contained approximately 30 columns,but columns 15 to 30 were completely empty and were therefore removed. Around 33% of the data was missing, particularly in the 'Nuclear' and 'Powerage' energy source fields.")
        st.text("Most of the remaining columns were of data types 'object' and 'float', which required conversion and preprocessing to enable accurate and meaningful analysis.")   
            

        # Ensure correct data types
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df["Year"] = df["Date"].dt.year
        df['Consommation (MW)'] = pd.to_numeric(df['Consommation (MW)'], errors='coerce')
        df['Région'] = df['Région'].fillna("Inconnue")
        df = df.dropna(subset=['Date', 'Consommation (MW)', 'Région'])
        return df

    if uploaded_file is not None:
        df = load_data(uploaded_file)
        
        st.subheader("🧹 Cleaned Data Preview")
        st.text("Our data is from ODRE (Open Data Energy Network).")
        st.text("Dataset: eco2mix-regional-cons-def.csv")
        st.text("Volume: 32 columns / 2.121.410 rows.")
         
        st.text("The data cleaning process involved removing unnecessary columns and eliminating rows with missing values in critical fields such as 'Date', 'Consumption', and 'Region'. These rows were excluded because they lacked essential information required for analysis and would not contribute meaningful insights. Retaining them could have introduced inaccuracies or bias into the results.")    
        df = df.drop(df.columns[15:32], axis=1)
        st.dataframe(df.head(10))
        st.text("The data types are bool(1), datetime64[ns](1), float64(12), int32(3), int64(2), object(4) memory usage: 333.8+ MB Unnecessary columns were removed :15-30")  
    image_path_c = "Introduction1.jpg"
    if os.path.exists(image_path_c):
        image = Image.open(image_path_c)
        st.image(image, caption="", use_container_width=True)
        image_path_c= "Introduction1.jpg"
    else:
        st.error(f"Image not found: {image_path_c}")
    image_path_d = "Introduction2.jpg"

    if os.path.exists(image_path_d):
        image = Image.open(image_path_d)
        st.image(image, caption="", use_container_width=True)
        
        image_path_d= "Introduction2.jpg"
    else:
        st.error(f"Image not found: {image_path_d}")
    image_path_d = "Introduction2.jpg"
    uploaded_file = "eco.csv"
    image_path_l = "Energy_image.jpg"
    if os.path.exists(image_path_l):
        image = Image.open(image_path_l)
        st.image(image, caption="", use_container_width=True)
        image_path_l= "Overview_PowerOutages_conclusion.jpg"
    else:
        st.error(f"Image not found: {image_path_l}")
if page == pages[2] :
    uploaded_file = "eco.csv"
    st.write("## Presentation of graphs")
    image_path_e = "Average_consumption_region1.jpg"    
    if os.path.exists(image_path_e): 
      image = Image.open(image_path_e)
      st.image(image, caption="", use_container_width=True)
    else:
      st.error(f"Image not found: {image_path_e}") 

    st.text("This bar chart displays the average electricity consumption (in megawatts) by region in France.")
    st.text("Each bar represents a different French region, with the height corresponding to the average consumption level.")
    st.text("Key observations: Île-de-France has the highest average consumption, followed closely by Auvergne-Rhône-Alpes.Regions like Centre-Val de Loire, Bourgogne-Franche-Comté, and Bretagne show the lowest average consumption.")
    st.text("The variation across regions likely reflects differences in population density, industrial activity, and climate.Overall, the chart provides a clear visual comparison of regional energy demands across France.")
    image_path_f = "Consumption_over_time2.jpg"    
    if os.path.exists(image_path_f): 
      image = Image.open(image_path_f)
      st.image(image, caption="", use_container_width=True)
    else:
      st.error(f"Image not found: {image_path_f}") 

    st.text("This line chart shows electricity consumption over time from 2013 to 2022, measured in megawatts (MW).")
  
    st.text("• There is a clear seasonal pattern with peaks occurring each winter and troughs in summer, indicating higher energy use during colder months—likely due to heating.")
    st.text("• The general trend appears relatively stable over the years, without a strong upward or downward drift.")
    st.text("• The sharp peaks and valleys highlight daily or weekly fluctuations layered within the broader seasonal cycle.")
    st.text("Overall, this graphic illustrates the cyclical nature of electricity demand in France, primarily driven by seasonal weather changes.")
    image_path_j = "Average_production_type.jpg"    
    if os.path.exists(image_path_j): 
      image = Image.open(image_path_j)
      st.image(image, caption="", use_container_width=True)
    else:
      st.error(f"Image not found: {image_path_j}") 
    st.text("This bar chart shows the average electricity production in France by energy type (in megawatts, MW).")
    st.text("Key points:")
    st.text("• Nuclear energy is by far the largest contributor to electricity production.")
    st.text("• Hydraulic (hydropower) is the second largest source, followed by thermal and wind (éolien) energy.")
    st.text("Overall, the graphic highlights France’s strong dependence on nuclear power, with renewables playing a smaller, though diverse, role in the energy mix.")
    st.text("• Solar, bioenergies, and pumped storage (pompage) contribute significantly less.")

    image_path_g = "Total_production_over_time3.jpg"    
    if os.path.exists(image_path_g): 
      image = Image.open(image_path_g)
      st.image(image, caption="", use_container_width=True)
    else:
      st.error(f"Image not found: {image_path_g}") 
    st.text("The graphic shows Total Production (MW) over time from late 2013 to early 2023.")
    st.text("It reveals a consistent annual cyclical pattern, with higher production during certain parts of the year. While production levels were relatively stable until mid-2021, there's a noticeable decline in total production from late 2021 onwards.According to some sources some maintenance work have been done also during this period. One of the reason of law prodcuctions.")
    image_path_h = "Production_Consumption4.jpg"    
    if os.path.exists(image_path_h): 
      image = Image.open(image_path_h)
      st.image(image, caption="", use_container_width=True)
    else:
      st.error(f"Image not found: {image_path_h}") 
    image_path_m = "Nucleare_production.jpg"    
    if os.path.exists(image_path_m): 
      image = Image.open(image_path_m)
      st.image(image, caption="", use_container_width=True)
    else:
      st.error(f"Image not found: {image_path_m}")

    st.text("Comments LN bold text Production generally tracks consumption closely, indicating effective grid management and supply-demand balancing. There are periods where production slightly exceeds consumption, suggesting a buffer for exports or grid stability. However, there are also brief intervals where consumption meets or slightly surpasses production, which may indicate moments of grid stress or the need for imports.")
    
    image_path_i = "Production_Consumption_time5.jpg"    
    if os.path.exists(image_path_i): 
      image = Image.open(image_path_i)
      st.image(image, caption="", use_container_width=True)
    else:
      st.error(f"Image not found: {image_path_i}") 

    st.text("This graph displays electricity production (red) and consumption (blue) in megawatts (MW) from roughly 2013 to 2022.Throughout the period, production consistently exceeds consumption. The gap between the red and blue lines represents surplus generation capacity, which is important for grid stability and export potential.However, both production and consumption appear to decrease toward the end of the period (2021–2022), which could reflect reduced demand (possibly due to economic factors or energy-saving measures) and/or constraints in generation capacity.")
    image_path_o = "Production_vs_Consumption_plotly.jpg"
    if os.path.exists(image_path_o):
        image = Image.open(image_path_o)
        st.image(image, caption="", use_container_width=True)
        image_path_o= "Production_vs_Consumption_plotly.jpg"
    else:
        st.error(f"Image not found: {image_path_k}")    
    st.text("This graph which take a closer look on one year : Jan 2022 to 2023 shows the same pattern as the above chart.The graph shows strong seasonal fluctuations, with clear peaks in both production and consumption during the winter months (early 2021, early 2022, and early 2023).However, the narrow margins during peak demand periods, combined with increasing volatility, mean that the risk of blackout is real—especially during extreme weather or if there are unexpected failures in generation or grid infrastructure.")
if page == pages[3] :
     st.subheader("Conclusion")
     image_path_k = "Overview_PowerOutages_conclusion.jpg"
     if os.path.exists(image_path_k):
        image = Image.open(image_path_k)
        st.image(image, caption="", use_container_width=True)
        image_path_k= "Overview_PowerOutages_conclusion.jpg"
     else:
        st.error(f"Image not found: {image_path_k}")
     st.text("From 2013 through early 2025, Frensh power system avoided a continuous nationwide blackout but experienced multiple significant regional and large-scale outages. These were driven by a combination of aging infrastructure, extreme weather events, technical failures, nuclear fleet maintenance challenges, and emerging security threats. The interconnected European grid both supports and complicates France’s electricity reliability, as demonstrated by the large-scale blackout events in 2025. Ongoing efforts focus on improving grid resilience, integrating renewables, and enhancing security measures."
     )
     image_path_l = "Energy_image.jpg"
     if os.path.exists(image_path_l):
        image = Image.open(image_path_l)
        st.image(image, caption="", use_container_width=True)
        image_path_l= "Overview_PowerOutages_conclusion.jpg"
     else:
        st.error(f"Image not found: {image_path_l}")


       