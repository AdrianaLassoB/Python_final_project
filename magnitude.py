import pandas as pd
import streamlit as st
import pydeck as pdk

def set_theme():
    # Update the default Streamlit theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: paleturquoise; /* Change this to the color you desire */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
st.title("Magnitude")
# Call the set_theme function to apply the custom theme
set_theme()

df_nuclear = pd.read_csv("nuclear_explosions.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)


st.write("To determine which bombs are the strongest, we analize the Data lower yield and the data upper yield, the higest these two numbers are, the strongest the bombs were")
from PIL import Image
img = Image.open("C:/Users/lasso/PycharmProjects/Final_project/pages/bombita.jpeg")
st.image(img, width= 500)
max_lower_yield = df_nuclear['Data.Yeild.Lower'].max()
max_upper_yield = df_nuclear['Data.Yeild.Upper'].max()

#[DA4]
df_nuclear['Total_Yield'] = df_nuclear['Data.Yeild.Lower'] + df_nuclear['Data.Yeild.Upper']
#[DA5]

highest_us = df_nuclear[df_nuclear['WEAPON_SOURCE_COUNTRY'] == 'USA'].nlargest(5, 'Total_Yield')

st.write("The five strongest bombs were of USA were",highest_us)

#[DA6] Filter data by two conditions

# Filter the DataFrame to show rows where either 'Data.Yeild.Lower' or 'Data.Yeild.Upper' equals the maximum values
max_yield_rows = df_nuclear[(df_nuclear['Data.Yeild.Lower'] == max_lower_yield) | (df_nuclear['Data.Yeild.Upper'] == max_upper_yield)]

st.write("According to these mesuares and our data", max_yield_rows ,"were the strongest bomb in between the years 1945-1998")

max_yield_rows.rename(columns={"Location.Cordinates.Latitude":"lat", "Location.Cordinates.Longitude": "lon"}, inplace= True)
view_state = pdk.ViewState(
latitude = max_yield_rows["lat"].mean(),  # The latitude of the view center
longitude = max_yield_rows["lon"].mean(),  # The longitude of the view center
# latitude= 20,
# longitude= 20,
zoom = 5,  # View zoom level
pitch = 0)  # Tilt level


layer1 = pdk.Layer(type='ScatterplotLayer',  # layer type
data = max_yield_rows,  # data source
get_position = '[lon, lat]',  # coordinates
get_radius = 1500,  # scatter radius
get_color = [100, 250, 30],  # scatter color
pickable = False  # work with tooltip
)


layer2 = pdk.Layer('ScatterplotLayer',
data = max_yield_rows,
get_position = '[lon, lat]',
get_radius = 1500,
get_color = [0, 0, 255],
pickable = True
)


# stylish tool tip: https://pydeck.gl/tooltip.html?highlight=tooltip
tooltip = {   "html": "Location: <b>{WEAPON_DEPLOYMENT_LOCATION}</b>",
    "style": {"backgroundColor": "white", "color": "steelblue"}}


# Create a map based on the view, layers, and tool tip
map = pdk.Deck(
map_style = 'mapbox://styles/mapbox/outdoors-v11',  # Go to https://docs.mapbox.com/api/maps/styles/ for more map styles
initial_view_state = view_state,
layers = [layer1, layer2],  # The following layer would be on top of the previous layers
tooltip = tooltip
)

st.pydeck_chart(map)