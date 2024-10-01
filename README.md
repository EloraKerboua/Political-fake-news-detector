# Political Fake News Detector

## Project Overview
This project aims to combat political misinformation targeting young, first-time voters in the U.S. The platform detects fake news and provides educational resources, empowering users to critically evaluate online information, especially in light of the upcoming 2024 elections.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Data Collection](#data-collection)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Sentiment Analysis](#sentiment-analysis)
- [Model Development](#model-development)
- [Future Development and Improvements](#future-development-and-improvements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used
- **Python**: The primary programming language.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For building machine learning models.
- **Natural Language Toolkit (NLTK)**: For text processing.
- **Streamlit**: For creating the interactive web application.
- **Matplotlib / Seaborn**: For data visualization.

## Data Collection
I merged two Kaggle datasets containing both fake and true news articles, building a robust foundation for training my models. The dataset comprises over 11,000 true articles and nearly 7,000 fake articles, which presented class imbalance that I addressed using SMOTE (Synthetic Minority Over-sampling Technique) combined with ENN (Edited Nearest Neighbors).

## Exploratory Data Analysis (EDA)
- **Temporal Analysis**: I observed significant trends in the frequency of fake news over time, noting spikes during critical political events such as the 2016 U.S. election and early 2017 around Donald Trump's inauguration.
  
- **Text Length Analysis**: My analysis revealed that fake news articles are generally longer than true news, with a t-test yielding a small p-value indicating significant differentiation based on text length.

## Sentiment Analysis
In my sentiment analysis, I found that fake news articles typically express a higher level of negative sentiment, while true news articles exhibit more neutral sentiment. This aligns with the notion that fake news often aims to evoke emotional responses, manipulating public opinion through emotionally charged language.

## Model Development
I trained several models to classify political news as fake or real, including:
- **Logistic Regression**: 91% accuracy.
- **Decision Tree**: 91% accuracy but lower precision for fake news.
- **Random Forest**: 94% accuracy with a robust balance between precision and recall.
- **Support Vector Machine (SVM)**: 94% accuracy, comparable to Random Forest.

Ultimately, I chose the Random Forest model for its robustness and reliability across both classes, minimizing false negatives while maintaining high accuracy.

## Future Development and Improvements
- **Model Enhancement**: Continuously refine machine learning models by incorporating new data and user feedback.
- **Content Expansion**: Broaden educational resources to cover more misinformation topics and enhance media literacy.
- **Community Engagement**: Foster a community where users can share insights and strategies to combat misinformation.

## Usage
To run the application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/political-fake-news-detector.git

2. **Navigate to the project directory**:
   ```bash
cd political-fake-news-detector

3. **Install the required dependencies**:
   ```bash
pip install -r requirements.txt

4. **Run the Streamlit app**:
   ```bash
streamlit run Home.py

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
