import streamlit as st
import requests

# Cache the quiz data to reduce API calls
@st.cache_data(ttl=60)  # Cache for 60 seconds
def fetch_quiz_questions():
    try:
        url = "https://opentdb.com/api.php?amount=5&type=multiple"
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()  # Parse the response as JSON

        # Check if 'results' exists in the response
        if 'results' in data:
            return data['results']
        else:
            st.error("Unexpected response format from the API. Please try again later.")
            return []

    except requests.exceptions.HTTPError as e:
        if response.status_code == 429:
            st.error("Too many requests. Please try again in a minute.")
        else:
            st.error(f"Failed to fetch quiz questions. Please try again later.")
        return []

    except Exception as e:
        st.error("An unexpected error occurred. Please try again later.")
        return []

def show_quizzes_page():
    st.title("Quizzes and Assessments")
    
    questions = fetch_quiz_questions()

    if questions:  # Only display the quizzes if questions were successfully fetched
        for i, question in enumerate(questions):
            st.subheader(f"Question {i+1}: {question['question']}")
            options = question['incorrect_answers'] + [question['correct_answer']]
            answer = st.radio(f"Select the correct answer for Question {i+1}:", options)
            if st.button(f"Submit Answer for Question {i+1}"):
                if answer == question['correct_answer']:
                    st.success("Correct!")
                else:
                    st.error("Incorrect! The correct answer was " + question['correct_answer'])
    else:
        st.warning("No quiz questions available at the moment.")

if __name__ == "__main__":
    show_quizzes_page()
