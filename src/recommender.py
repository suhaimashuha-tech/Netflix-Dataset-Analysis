from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_model(df):
    tfidf = TfidfVectorizer(stop_words="english")
    matrix = tfidf.fit_transform(df["content"])
    similarity = cosine_similarity(matrix)
    return similarity

def recommend(title, df, similarity):
    indices = df.index[df["title"] == title].tolist()
    
    if not indices:
        return ["Title not found"]
    
    idx = indices[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    return df["title"].iloc[[i[0] for i in scores]].tolist()