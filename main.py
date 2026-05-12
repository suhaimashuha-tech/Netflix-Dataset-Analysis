import sys
sys.path.append("src")

from data_loader import load_data
from preprocessing import clean_data, create_features
from recommender import build_model, recommend

def main():
    print("Loading data...")

    df = load_data("data/netflix_titles.csv")
    df = clean_data(df)
    df = create_features(df)

    # ======================
    # 📊 DATA ANALYSIS
    # ======================

    print("\n📊 Total Movies vs TV Shows:")
    print(df["type"].value_counts())

    print("\n🌍 Top 5 Countries:")
    print(df["country"].value_counts().head())

    print("\n🎭 Most Common Genres:")
    print(df["listed_in"].value_counts().head())

    print("\n📅 Content Over Years:")
    print(df["release_year"].value_counts().head())

    # ======================
    # 🎬 RECOMMENDER
    # ======================

    similarity = build_model(df)

    movie = input("\nEnter a movie name: ")

    results = recommend(movie, df, similarity)

    print("\nRecommendations:")
    for r in results:
        print("-", r)

if __name__ == "__main__":
    main()