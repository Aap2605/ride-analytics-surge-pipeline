import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pipeline/production_ride_data.csv")

st.title("Real-Time Ride Analytics Dashboard")

st.subheader("Ride Data Preview")
st.dataframe(df.head())

st.subheader("Ride Status Count")

status_counts = df["ride_status"].value_counts()

fig, ax = plt.subplots()
ax.bar(status_counts.index, status_counts.values)

st.pyplot(fig)