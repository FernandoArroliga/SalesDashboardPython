# Importing the useful libraries and modules
import pandas as pd
import plotly.express as px
import streamlit as st

# Load the data
data = pd.read_csv("supermarket_sales.csv")

# Set the page configuration
# emojis url: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

# Display dataframe into streamlit app
st.dataframe(data)

