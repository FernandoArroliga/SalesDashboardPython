# Importing the useful libraries and modules
import pandas as pd
import plotly.express as px
import streamlit as st

# Load the data
data = pd.read_csv("supermarket_sales.csv")

# Cleaning the data
data = data.rename(columns={
    "Invoice ID": "Invoice_ID",
    "Customer type": "Customer_Type",
    "Product line": "Product_Line",
    "Unit price": "Unit_Price",
    "gross margin percentage": "Gross_Margin_Percentage",
    "gross income": "Gross_Income"
    })


# Set the page configuration
# emojis url: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

# Create Streamlit Widgets

# -------- SIDEBAR ---------------
st.sidebar.header("Please Filter Here:")

city = st.sidebar.multiselect(
    "Select the City:",
    options=data["City"].unique(),
    default=data["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=data["Customer_Type"].unique(),
    default=data["Customer_Type"].unique()
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=data["Gender"].unique(),
    default=data["Gender"].unique()
)

data_selection = data.query(
    "City == @city & Customer_Type == @customer_type & Gender == @gender"
)

# ---------- MAINPAGE ------------------
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI´S
total_sales = int(data_selection["Total"].sum())
average_rating = round(data_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sales_by_transaction = round(data_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sales_by_transaction}")

st.markdown("---")    

# SALES BY PRODUCT LINE (BAR CHART)
sales_by_product_line = (
    data_selection.groupby(by=["Product_Line"]).sum()[["Total"]].sort_values(by="Total")
)

fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

st.plotly_chart(fig_product_sales)
# Display dataframe into streamlit app
#st.dataframe(data_selection)
