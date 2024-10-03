import streamlit as st

def run_home():
    # Introduction text from main.py
    st.title("Welcome to the Political Fake News Detector")
    st.write(
        """
        This platform empowers young voters to critically assess political news, especially during key events such as elections. 
        Navigate through the app to learn more about misinformation, analyze news content, and gain insights into disinformation trends.
        
        **What is Fake News?** 
        Fake news refers to false or misleading information presented as news. It is often created to influence public opinion, generate clicks, or promote a specific agenda. Identifying fake news is crucial to staying informed and making well-reasoned decisions.
        """
    )

    # Added Features Section
    st.subheader("Explore Our Features")
    st.write(
        """
        Our platform includes several modules designed to enhance your understanding of fake news and misinformation:
        
        - **Fake News Detector:** This module allows you to input text and get an analysis of whether the content is likely to be fake or true. It leverages advanced NLP and machine learning techniques to provide accurate assessments.
        - **Quiz:** Test your knowledge with our interactive quiz designed to help you recognize fake news articles. It's a fun and educational way to improve your ability to spot misinformation.
        """
    )

    # Content previously in home.py
    st.header("Understanding Misinformation During US Elections")
    st.write(
        """
        Misinformation during elections is a serious concern, as it can influence voters' opinions, shape political discourse, 
        and even affect election outcomes. Various tactics, such as emotionally charged language, misleading headlines, 
        and fabricated stories, are commonly used to sway public perception.
        """
    )

    st.subheader("Key Political Events and Misinformation")
    st.write(
        """
        Understanding how misinformation spikes around major events can help identify patterns and potential disinformation campaigns. 
        Always stay informed and critically assess the information you encounter.
        """
    )

    # Image section
    st.subheader("Temporal Trends in Political News Articles")
    image_path = 'C:/Users/elora/Desktop/IRONHACK/PROJECTS/FINAL PROJECT FAKE NEWS/DATA AND NOTEBOOKS/images/temporal_trends.png'
    st.image(image_path, caption="Temporal Trends in Fake News Frequency")

    # Brief interpretation of the graph
    st.write(
        """
        The graph reveals a significant increase in fake news around key political events. For instance, there is a spike around the 
        2016 election period, indicating that misinformation becomes more prevalent during these crucial times. This underscores the 
        importance of using tools like our Fake News Detector to stay informed and critically evaluate the information presented, especially with the upcoming 2024 elections.
        """
    )

    # Quiz introduction
    st.write(
        """
        Ready to test your knowledge? Navigate to the 'Quiz' section to take our interactive quiz and see how well you can spot fake news!
        """
    )

# Run the home function
if __name__ == "__main__":
    run_home()
