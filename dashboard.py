import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pipeline/production_ride_data.csv")

st.title("🚖 Real-Time Ride Analytics Dashboard")

# KPI Cards
total_rides = len(df)
completed_rides = len(df[df["ride_status"] == "COMPLETED"])
cancelled_rides = len(df[df["ride_status"] == "CANCELLED"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Rides", total_rides)
col2.metric("Completed", completed_rides)
col3.metric("Cancelled", cancelled_rides)

# Data Preview
st.subheader("Ride Data Preview")
st.dataframe(df.head())

# Ride Status Chart
st.subheader("Ride Status Count")

status_counts = df["ride_status"].value_counts()

fig, ax = plt.subplots()
ax.bar(status_counts.index, status_counts.values)

st.pyplot(fig)

# Location Analytics
st.subheader("Top Pickup Locations")

location_counts = df["pickup_location"].value_counts()

fig2, ax2 = plt.subplots()
ax2.bar(location_counts.index, location_counts.values)

plt.xticks(rotation=45)

st.pyplot(fig2)