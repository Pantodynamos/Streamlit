import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Dashboard for Shared Bike Riding Data Analysis')

st.image("Cloaked_figure.png")

df = pd.read_csv("day.csv")

st.dataframe(df)

plt.figure(figsize=(10, 6))
plt.plot(df['mnth'], df['cnt'], marker='o', linestyle='-')
plt.title('Total User Count and Month')
plt.xlabel('Month')
plt.ylabel('Total User Count')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
plt.show()
