import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Dashboard for Shared Bike Riding Data Analysis')

st.image("Cloaked_figure.png")

df = pd.read_csv("day.csv")

st.dataframe(df)
st.write("Dibawah adalah chart untuk perbandingan total pengguna per bulan")
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    df["mnth"],
    df["cnt"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)
