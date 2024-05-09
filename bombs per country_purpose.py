import pandas as pd
import streamlit as st
import pydeck as pdk
def set_theme():
    # Update the default Streamlit theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: violet; /* Change this to the color you desire */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Call the set_theme function to apply the custom theme
set_theme()
df_nuclear = pd.read_csv("nuclear_explosions.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)

#[ST2] I was able to change the aligment of the title and the color with the help of chat gpt
title_style = """
    <style>
    .title {
        text-align: center;
        color: aquamarine;
    }
    </style>
"""

# Apply the style for centering the title
st.markdown(title_style, unsafe_allow_html=True)

# Display the centered title
st.markdown("<h1 class='title'>Bombs per country</h1>", unsafe_allow_html=True)

Suma = 0



purpose = []


for row in df_nuclear.itertuples():
    if row.data_Purpose not in purpose:
        purpose.append(row.data_Purpose)

#[DA 2] drop values
purpose.remove('Se')
purpose.remove('Sb')
purpose.remove('Pne:Plo')
purpose.remove('Pne:V')
purpose.remove('Nan')
purpose.remove('Wr/Se')
purpose.remove('Wr/We')
purpose.remove('Wr/Pne')
purpose.remove('Wr/Sam')
purpose.remove('Pne/Wr')
purpose.remove('Se/Wr')
purpose.remove('Wr/P/Sa')
purpose.remove('We/Sam')
purpose.remove('We/Wr')
purpose.remove('Wr/F/Sa')
purpose.remove('Wr/Fms')
purpose.remove('Fms/Wr')
purpose.remove('Wr/P/S')
purpose.remove('Wr/F/S')
purpose.remove('Wr/We/S')
print(purpose)

#[ST3]
selected_purpose1 = st.selectbox("Please select the Purpose you would like to know the meaning of", purpose)



#[PY2] A dictionary where you write code to acces its keys, values or items
meaning ={}
meaning['Combat']=' :For combating purposes'
meaning['Fms'] =' :To study the phenomena of a nuclear explotions'
meaning['Me'] = ': Test conducted in the context of a military exercise with a real nuclear detonation.'
meaning['Pne'] = ' :Peaceful nuclear explosion.'
meaning['Sam']=' :Tests to study accidental modes and emergencies.'
meaning['Transp'] =' :Transportation-storage purposes'
meaning['We'] =' :To evaluate the effects of a nuclear detonation on various targets.'
meaning['Wr'] = ' :related to the weapon development.'
if selected_purpose1:
    st.write(selected_purpose1,meaning[selected_purpose1])

countries = []

for row in df_nuclear.itertuples():
    if row.WEAPON_SOURCE_COUNTRY not in countries:
        countries.append(row.WEAPON_SOURCE_COUNTRY )




import streamlit as st
import pandas as pd



# Get unique countries
countries = df_nuclear['WEAPON_SOURCE_COUNTRY'].unique()



#[ST4]
selected_country = st.radio("Please select a Country", countries)

#[PY 3]
def calculate_country_percentage( country,df = df_nuclear):
    total_bombs = len(df)
    country_bombs = len(df[df['WEAPON_SOURCE_COUNTRY'] == country])
    percentage = (f'{(country_bombs / total_bombs) * 100:.2f}')
    return percentage

st.write("The country", selected_country,"was responsable for", calculate_country_percentage(selected_country),"% of bombs")


#[EXTRA CREDIT] imported plotly with is a package for more complex graphs
import plotly.graph_objs as go

#[DA 3] FILTER DATA
selected_country_data = df_nuclear[df_nuclear['WEAPON_SOURCE_COUNTRY'] == selected_country]

# Count occurrences of each purpose for the selected country
purpose_counts = selected_country_data['data_Purpose'].value_counts()

#[VIZ2]
# Create a pie chart for the purpose distribution
fig = go.Figure(data=[
    go.Pie(labels=purpose_counts.index, values=purpose_counts.values)
])

# Customize layout
fig.update_layout(
    title=f"Purpose Distribution in {selected_country}"
)

# Plot the pie chart
st.plotly_chart(fig, use_container_width=True)







# Plot the purpose distribution for the selected country with tooltips
Suma = 0
for row in df_nuclear.itertuples():
    if row.WEAPON_SOURCE_COUNTRY == selected_country:  # Convert year to string for comparison
        Suma += 1

st.write("The country", selected_country, "has dropped a total of", Suma,"bombs in between 1945 and 1998")

df_selected_country = df_nuclear[df_nuclear['WEAPON_SOURCE_COUNTRY'] == selected_country]





#[VIZ3]
df_selected_country.rename(columns={"Location.Cordinates.Latitude":"lat", "Location.Cordinates.Longitude": "lon"}, inplace= True)
view_state = pdk.ViewState(
latitude = df_selected_country["lat"].mean(),  # The latitude of the view center
longitude = df_selected_country["lon"].mean(),  # The longitude of the view center
# latitude= 20,
# longitude= 20,
zoom = 5,  # View zoom level
pitch = 0)  # Tilt level

# Create a map layer with the given coordinates
layer1 = pdk.Layer(type='ScatterplotLayer',  # layer type
data = df_selected_country,  # data source
get_position = '[lon, lat]',  # coordinates
get_radius = 100000,  # scatter radius
get_color = [100, 250, 30],  # scatter color
pickable = False  # work with tooltip
)

# Can create multiple layers in a map
# For more layer information
# https://deckgl.readthedocs.io/en/latest/layer.html
# Line layer https://pydeck.gl/gallery/line_layer.html
layer2 = pdk.Layer('ScatterplotLayer',
data = df_selected_country,
get_position = '[lon, lat]',
get_radius = 100000,
get_color = [0, 0, 255],
pickable = True
)


# stylish tool tip: https://pydeck.gl/tooltip.html?highlight=tooltip
tooltip = {   "html": "Location: <b>{WEAPON_DEPLOYMENT_LOCATION}</b> Purpose: <b>{data_Purpose}</b>",
    "style": {"backgroundColor": "white", "color": "steelblue"}}


# Create a map based on the view, layers, and tool tip
map = pdk.Deck(
map_style = 'mapbox://styles/mapbox/satellite-streets-v12',  # Go to https://docs.mapbox.com/api/maps/styles/ for more map styles
initial_view_state = view_state,
layers = [layer1, layer2],  # The following layer would be on top of the previous layers
tooltip = tooltip
)

st.pydeck_chart(map)







df_selected_country = df_nuclear[df_nuclear['WEAPON_SOURCE_COUNTRY'] == selected_country]

# Count the occurrences of each purpose for the selected country


#[PY 3] did it with help of chatgpt, at the end I was not able to use the information but it helped to get an idea of how the data was distributed
purposes = ['combat', 'fms', 'me', 'pne', 'sam', 'sse', 'transp', 'we', 'wr']

# Use a list comprehension to count occurrences of each purpose
purpose_counts = {purpose.upper(): sum(1 for row in df_nuclear.itertuples() if getattr(row, 'data_Purpose').lower() == purpose) for purpose in purposes}



df_nuclear['Date_Year'] = pd.to_datetime(df_nuclear['Date_Year'], format='%Y')
bombs_dropped_by_year_country = df_nuclear.groupby(['Date_Year', 'data_Purpose']).size().unstack(fill_value=0)


# Display the line chart [ST3]
st.title("Distribution of the bombs's purposes through out the years")
st.line_chart(bombs_dropped_by_year_country)


