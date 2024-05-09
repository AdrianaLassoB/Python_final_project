

import pandas as pd
import streamlit as st

#For all the colors inthe background I was used Chat gpt
def set_theme():
    # Update the default Streamlit theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: mintcream; /* Change this to the color you desire */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Call the set_theme function to apply the custom theme
set_theme()

df_nuclear = pd.read_csv("nuclear_explosions.csv")
list_selected =["WEAPON_DEPLOYMENT_LOCATION","WEAPON_SOURCE_COUNTRY"]
comlums_selected = df_nuclear[list_selected]

st.title("Nuclear explosions between 1945 and 1998")
from PIL import Image
img = Image.open("C:/Users/lasso/PycharmProjects/Final_project/pages/nuclear.jpeg")
st.image(img, width= 500, )
st.write("In this page we are going analize the nuclear bombs data from 1945 to 1998. For it we have three pages which divided the content between year, purpose and magnitude.")
st.write()
st.write()
st.write("As an insight of how the data looks, here are the firts ten rows")
#[PY 1]
def display(df):
    return df.shape, df.head(10)

number_rows, firts_10_rows = display(df_nuclear)
st.write("The data contains",number_rows[0],"rows")
st.write(firts_10_rows)


