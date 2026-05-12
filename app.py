import sys
sys.path.append("src")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from data_loader import load_data
from preprocessing import clean_data, create_features
from recommender import build_model, recommend

st.title("🎬 Netflix Dataset Analysis & Recommender")

# Load data
df = load_data("data/netflix_titles.csv")
df = clean_data(df)
df = create_features(df)

# ======================
# 📊 ANALYSIS SECTION
# ======================

st.header("📊 Dataset Analysis")

# Movies vs TV Shows
st.subheader("Movies vs TV Shows")
type_counts = df["type"].value_counts()
st.bar_chart(type_counts)

# Top Countries
st.subheader("Top 5 Countries")
country_counts = df["country"].fillna("Unknown").value_counts().head()
st.bar_chart(country_counts)

# Genres
st.subheader("Top Genres")
genre_counts = df["listed_in"].value_counts().head()
st.bar_chart(genre_counts)

# Release Years
st.subheader("Content Over Years")
year_counts = df["release_year"].value_counts().head(10)
st.line_chart(year_counts)

# ======================
# 🎬 RECOMMENDER SECTION
# ======================

st.header("🎬 Movie Recommender")

similarity = build_model(df)

movie = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    results = recommend(movie, df, similarity)

    st.subheader("Recommendations:")
    for r in results:
        st.write("👉", r)