import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Dashboard for Shared Bike Riding Data Analysis')

st.image("bike_sharing.jpg")

df = pd.read_csv("day.csv")
dfhour = pd.read_csv("hour.csv")

st.write("Dibawah adalah data pengguna bike sharing per hari")
st.dataframe(df)
st.write("Dibawah adalah data pengguna bike sharing per jam")
st.dataframe(dfhour)

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

st.write("Dibawah adalah chart perbandingan total pengguna per jam pada hari kerja dan hari libur")

fig1, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=dfhour, x='hr', y='cnt', hue='weekday', ax=ax)
ax.set(title='Count of bikes at weekdays and weekends')

st.pyplot(fig1)

st.Header("Kesimpulan")
st.write("Dari chart pertama terlihat bahwa adanya peningkatan pengguna bike sharing pada bulan 5-9 yang berarti lebih banyak pengguna bike sharing pada musim summer dan fall,sedangkan pada musim winter dan spring terjadi penurunan. Lalu pada chart kedua terlihat peningkatan signifikan pada jam berangkat dan pulang kerja, sedangkan pada hari libur pengguna bike sharing meningkat setelah jam 10.")
