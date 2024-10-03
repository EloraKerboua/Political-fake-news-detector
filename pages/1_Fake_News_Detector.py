import streamlit as st
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the pre-trained model and vectorizer
model_path = 'C:/Users/elora/Desktop/IRONHACK/PROJECTS/FINAL PROJECT FAKE NEWS/DATA AND NOTEBOOKS/streamlit_app/Models/random_forest.pkl'
vectorizer_path = 'C:/Users/elora/Desktop/IRONHACK/PROJECTS/FINAL PROJECT FAKE NEWS/DATA AND NOTEBOOKS/streamlit_app/Models/tfidf_vectorizer.pkl'

with open(model_path, 'rb') as model_file, open(vectorizer_path, 'rb') as vectorizer_file:
    model = pickle.load(model_file)
    vectorizer = pickle.load(vectorizer_file)

# Streamlit app for Fake News Detector
st.title('Fake News Detector')
st.write('Enter the news text to analyze:')

# User input
news_text = st.text_area('')

# Analyze the input text when button is clicked
if st.button('Analyze'):
    if news_text:
        # Vectorize the input text
        input_vector = vectorizer.transform([news_text])
        
        # Make prediction
        prediction = model.predict(input_vector)[0]
        
        # Display result
        if prediction == 0:  # Assuming 0 = Fake and 1 = True
            st.write('This news article is likely **Fake**.')
            st.write('**Explanation:** This article may contain markers commonly associated with misinformation.')
        
        else:
            st.write('This news article is likely **True**.')
            st.write('**Explanation:** This article does not contain markers commonly associated with misinformation.')
    else:
        st.write('Please enter some text to analyze.')

# Adding disclaimer
st.markdown('---')
st.markdown(
    """
    *Disclaimer:* This analysis is based on a machine learning model and may contain errors. Please conduct further research before determining the truth of any news.
    """
)




