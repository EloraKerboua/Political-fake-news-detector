import streamlit as st

def run_quiz():
    st.title("Fake News Recognition Quiz")
    
    # Initialize score
    score = 0
    total_questions = 10

    # Define questions, options, and correct answers
    questions = [
        {
            "question": "Which of the following headlines seems the most suspicious?",
            "options": [
                "Select an option",  # Placeholder
                "Government announces new policy for small businesses.",
                "Aliens Land on Earth and Demand Our Wi-Fi!",
                "Local farmer wins award for best organic produce."
            ],
            "answer": "Aliens Land on Earth and Demand Our Wi-Fi!"
        },
        {
            "question": "Which source is the most reliable?",
            "options": [
                "Select an option",
                "A social media post from an unverified account.",
                "An article published by a reputable news outlet.",
                "A message forwarded multiple times on a messaging app."
            ],
            "answer": "An article published by a reputable news outlet."
        },
        {
            "question": "What should you do if a headline seems too sensational to be true?",
            "options": [
                "Select an option",
                "Share it immediately.",
                "Verify it with other credible sources.",
                "Ignore it."
            ],
            "answer": "Verify it with other credible sources."
        },
        {
            "question": "What is a common tactic used in fake news?",
            "options": [
                "Select an option",
                "Clear citations from experts.",
                "Outlandish claims without evidence.",
                "Balanced reporting."
            ],
            "answer": "Outlandish claims without evidence."
        },
        {
            "question": "Which of these signals that a news article might be fake?",
            "options": [
                "Select an option",
                "Numerous spelling and grammatical errors.",
                "Well-researched facts.",
                "Quotes from verified sources."
            ],
            "answer": "Numerous spelling and grammatical errors."
        },
        {
            "question": "Why is it important to check the publication date of a news article?",
            "options": [
                "Select an option",
                "Because newer articles are always more credible.",
                "To ensure the information is still relevant.",
                "It doesn’t matter; only the content is important."
            ],
            "answer": "To ensure the information is still relevant."
        },
        {
            "question": "Which website ending is generally more reliable?",
            "options": [
                "Select an option",
                ".com",
                ".gov",
                ".net"
            ],
            "answer": ".gov"
        },
        {
            "question": "How can reverse image searches help identify fake news?",
            "options": [
                "Select an option",
                "By finding the original source of an image.",
                "By making the image appear more credible.",
                "By automatically fact-checking the image."
            ],
            "answer": "By finding the original source of an image."
        },
        {
            "question": "What should you do if a news article lacks author information?",
            "options": [
                "Select an option",
                "Trust it because it's online.",
                "Question its credibility.",
                "Share it to get more opinions."
            ],
            "answer": "Question its credibility."
        },
        {
            "question": "Which of these is a sign of a clickbait headline?",
            "options": [
                "Select an option",
                "Accurate summary of the article.",
                "Vague claims that make you want to click to learn more.",
                "Clear citation of facts."
            ],
            "answer": "Vague claims that make you want to click to learn more."
        }
    ]

    # Loop through questions
    for i, q in enumerate(questions):
        st.write(f"{i + 1}. {q['question']}")
        answer = st.radio(f"Choose an option for Question {i + 1}:", q['options'], key=f"question_{i + 1}")

        # Check if the user has selected an option other than the placeholder
        if answer != "Select an option":
            if answer == q['answer']:
                st.success("Correct!")
                score += 1
            else:
                st.error("Not quite.")
        else:
            st.warning("Please select an option!")

    # Show final score
    st.write("## Your final score:")
    st.write(f"You scored {score} out of {total_questions}.")

    # Optional: Provide feedback based on score
    if score == total_questions:
        st.balloons()
        st.write("🎉 Excellent! You're a fake news detection pro!")
    elif score >= total_questions / 2:
        st.write("👍 Good job! You have a solid understanding, but there's room to improve.")
    else:
        st.write("🤔 Keep practicing! Identifying fake news takes time and critical thinking.")

# Run the quiz function
if __name__ == "__main__":
    run_quiz()
