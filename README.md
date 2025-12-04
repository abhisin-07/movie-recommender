🎬 Movie Recommendation System (Content-Based Filtering)

A simple yet powerful Movie Recommendation System built using Machine Learning, NLP, and Streamlit.
This project recommends movies based on their genres, keywords, and overview descriptions using TF-IDF Vectorization and Cosine Similarity.

🚀 Features

📌 Content-Based Recommender (no user history required)

🔍 Uses TF-IDF to convert text data into meaningful vectors

📏 Computes movie similarity using Cosine Similarity

🎥 Enter a movie name → get Top 5 similar movies

🌐 Interactive web app built with Streamlit

⚡ Fast performance using pre-saved (pickled) model files

🧠 How It Works (Project Flow)
1️⃣ Data Cleaning & Preprocessing

Handled missing values

Cleaned genres and keywords using ast.literal_eval

Lowercased and tokenized text

Combined multiple text columns into a single features column

2️⃣ Text Vectorization (TF-IDF)

Converted movie descriptions into numerical vectors using:

TfidfVectorizer(max_features=5000, stop_words='english')

3️⃣ Similarity Computation

Used Cosine Similarity to measure how close two movies are based on their TF-IDF vectors.

4️⃣ Recommendation Engine

A custom recommend() function:

Finds the selected movie

Sorts all movies by similarity score

Returns the top 5 similar movies

5️⃣ Streamlit Web App

Interactive app where users can:

Type a movie name

Click Recommend

Instantly see similar movie suggestions

🗂 Project Files
📁 Movie-Recommendation-System/
│── app.py                # Streamlit app
│── movies.pkl            # Cleaned movies dataset
│── similarity.pkl        # Cosine similarity matrix
│── movie_dataset.csv     # (Optional) Raw dataset
│── notebook.ipynb        # Jupyter notebook with full ML pipeline
│── README.md             # Project documentation

💻 Installation & Running the App
1. Install dependencies
pip install -r requirements.txt

2. Run Streamlit app
streamlit run app.py

🛠 Tech Stack

Python

Pandas

NumPy

Scikit-learn

Streamlit

Pickle

🌟 Future Improvements

Add movie posters (using TMDB API)

Add user-based collaborative filtering

Deploy on Streamlit Cloud or HuggingFace Spaces

Use Word2Vec / BERT embeddings for deeper similarity
