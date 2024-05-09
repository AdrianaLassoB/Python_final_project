import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def set_theme():
    # Update the default Streamlit theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: lightgoldenrodyellow; /* Change this to the color you desire */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# Call the set_theme function to apply the custom theme
set_theme()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Bombs per year")
df_nuclear = pd.read_csv("nuclear_explosions.csv")

#[DA 1]
df_nuclear = df_nuclear.sort_values(by='Data.Magnitude.Surface', ascending= True)





years = []
for row in df_nuclear.itertuples():
    if row.Date_Year not in years:
        years.append(row.Date_Year)

from PIL import Image
img = Image.open("C:/Users/lasso/PycharmProjects/Final_project/pages/nuclear bombs.jpeg")
st.image(img, width= 500)

#[ST1]
slider_number = st.slider("Please select the year ypu would like to how many bombs were dropped", years[0],years[-1])


from PIL import Image

Suma = 0  # Initialize LOLA outside the loop
for row in df_nuclear.itertuples():
    if row.Date_Year == slider_number:  # Convert year to string for comparison
        Suma += 1


st.write("The amount of bombs dropped in",slider_number,"is",Suma)


df_selected_year = df_nuclear[df_nuclear['Date_Year'] == int(slider_number)]

# Plot distribution of weapon source countries for the selected year
if Suma > 0:
    df_selected_year['WEAPON_SOURCE_COUNTRY'].value_counts().plot(kind='bar',color=["red", "orange", "blue", "green", "yellow"])
    plt.xlabel("Source Countries")
    st.pyplot()




st.title("Bombs Dropped Over Years by Country")
df_nuclear['Date_Year'] = pd.to_datetime(df_nuclear['Date_Year'], format='%Y')
bombs_dropped_by_year_country = df_nuclear.groupby(['Date_Year', 'WEAPON_SOURCE_COUNTRY']).size().unstack(fill_value=0)




#[VIZ1]
# Display the line chart
st.line_chart(bombs_dropped_by_year_country)


