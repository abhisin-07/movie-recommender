import streamlit as st
import pandas as pd
import pickle

# Load the data
movies = pickle.load(open('data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie_name):
    movie_name = movie_name.lower()
    try:
        idx = movies[movies['title'].str.lower() == movie_name].index[0]
    except:
        return ["Movie not found."]
    
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_5 = sorted_scores[1:6]

    recommendations = []
    for i in top_5:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations

# Streamlit UI
st.title("🎬 Movie Recommendation System")
st.write("Find similar movies based on genres, keywords, and overview.")

selected_movie = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    results = recommend(selected_movie)
    
    st.write("### Recommended Movies:")
    for movie in results:
        st.write("➡️ ", movie)
