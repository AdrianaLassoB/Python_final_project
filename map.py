import streamlit as st
import pandas as pd

def set_theme():
    # Update the default Streamlit theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: navy; /* Change this to the color you desire */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Call the set_theme function to apply the custom theme
set_theme()
df_nuclear = pd.read_csv("nuclear_explosions.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)

title_style = """
    <style>
    .title {
        text-align: center;
        color: white;
    }
    </style>
"""

# Apply the style for centering the title
st.markdown(title_style, unsafe_allow_html=True)

# Display the centered title
st.markdown("<h1 class='title'>Bomb's deployment</h1>", unsafe_allow_html=True)

import pydeck as pdk
import streamlit as st


import streamlit as st
import pandas as pd
import pydeck as pdk

df_nuclear = pd.read_csv("nuclear_explosions.csv")



df_nuclear.rename(columns={"Location.Cordinates.Latitude":"lat", "Location.Cordinates.Longitude": "lon"}, inplace= True)


icon_data = {
    "url" : "https://upload.wikimedia.org/wikipedia/commons/5/57/Explosion-155624_icon.svg",
    "width": 100,
    "height": 100,
    "anchorY" : 100
}

df_nuclear["icon_data"]= None
for i in df_nuclear.index:
    df_nuclear["icon_data"][i]=icon_data

icon_layer = pdk.Layer(
    type = "IconLayer",
    data = df_nuclear,
    get_icon = "icon_data",
    get_position = '[lon,lat]',
    get_zise = 10,
    size_scale = 10,
    pickable = True
)

df_nuclear.rename(columns={"Location.Cordinates.Latitude": "lat", "Location.Cordinates.Longitude": "lon"},
                  inplace=True)

mp_df = df_nuclear[['WEAPON_DEPLOYMENT_LOCATION', 'lon', 'lat']]

view_state = pdk.ViewState(
    latitude=mp_df["lat"].mean(),
    longitude=mp_df["lon"].mean(),
    zoom=2,
    pitch= 0)

tooltip = {"html": "Location: <b>{WEAPON_DEPLOYMENT_LOCATION}</b>", "style": {"backgroundColor": "white", "color": "steelblue"}}
#[VIZ4]
map = pdk.Deck(
    map_style='mapbox://styles/mapbox/outdoors-v11',
    initial_view_state=view_state,
    layers=[icon_layer],
    tooltip=tooltip
)
st.pydeck_chart(map)













