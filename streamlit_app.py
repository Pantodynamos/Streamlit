import streamlit as st
import pandas as pd
import numpy as np

st.title('Dashboard for Shared Bike Riding Data Analysis')

uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
