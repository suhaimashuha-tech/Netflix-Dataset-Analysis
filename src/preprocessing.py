def clean_data(df):
    df = df.dropna(subset=["title", "description"])
    return df

def create_features(df):
    df["content"] = df["title"] + " " + df["description"]
    return df