import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Dashboard for Shared Bike Riding Data Analysis')

uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.image("Cloaked_figure.png")

bike_dataframe_day = pd.read_csv("day.csv")

bike_dataframe_day.head()

st.dataframe("bike_dataframe_day")
st.dataframe("day.csv")
min_date = bike_dataframe_day["dteday"].min()
max_date = bike_dataframe_day["dteday"].max()

with st.sidebar:

  start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
