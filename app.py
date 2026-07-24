import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# Streamlit Dashboard................................
st.set_page_config(page_title="IPL Interactive Dashboard", layout="wide")
st.title("IPL Streamlit Data Dashboard")

# File Upload
matches=pd.read_csv("matches_cleaned.csv")
delivery=pd.read_csv("deliveries_cleaned.csv")

st.subheader("Dataset Info")
st.write(matches.describe())
st.write(delivery.describe())

# Column Selection
numeric_cols=matches.select_dtypes(include=['float64','int64']).columns
st.sidebar.header("Filters")
season = st.sidebar.selectbox(
    "Select Season",
    sorted(matches["season"].unique())
)
filtered_matches = matches[matches["season"] == season]
filtered_deliveries = delivery[
    delivery["match_id"].isin(filtered_matches["id"])
]

# 1.Bar Chart
st.subheader(f"Matches By City- Season {season}")
city_count = filtered_matches["city"].value_counts()
fig, ax = plt.subplots(figsize=(8,4))
city_count.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
plt.ylabel("Number of Matches")
st.pyplot(fig)

# 2. Bar Chart
st.subheader(f"Winning Teams")
winner_count = filtered_matches["winner"].value_counts()
fig2, ax2 = plt.subplots(figsize=(8,4))
winner_count.plot(kind="bar", ax=ax2)
plt.xticks(rotation=45)
plt.ylabel("Number of Wins")
st.pyplot(fig2)

# Histogram
st.subheader(f"Top 10 Batsmen")
top_batsmen = (
    filtered_deliveries.groupby("batter")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
fig3, ax3 = plt.subplots(figsize=(8,4))
top_batsmen.plot(kind="bar", ax=ax3)
plt.xticks(rotation=45)
plt.ylabel("Total Runs")
st.pyplot(fig3)

# Live Data Table...........................
print("Live DATA Table")
st.subheader("Filtered Match Data")
st.dataframe(filtered_matches)

# Live API Card
st.markdown("---")
st.subheader("💡 Motivational Quote of the Day")

try:
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    data = response.json()

    quote = data[0]["q"]
    author = data[0]["a"]

    st.success(f'"{quote}"')
    st.write(f"**— {author}**")

except Exception:
    st.error("Unable to fetch quote.")