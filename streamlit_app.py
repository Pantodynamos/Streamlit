import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Dashboard for Shared Bike Riding Data Analysis')

st.image("Cloaked_figure.png")

df = pd.read_csv("day.csv")

st.write(df)
