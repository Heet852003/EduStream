import streamlit as st
import requests

def fetch_quiz_questions():
    url = "https://opentdb.com/api.php?amount=5&type=multiple"
    response = requests.get(url).json()
    return response['results']

def show_quizzes_page():
    st.title("Quizzes and Assessments")
    
    questions = fetch_quiz_questions()

    for i, question in enumerate(questions):
        st.subheader(f"Question {i+1}: {question['question']}")
        options = question['incorrect_answers'] + [question['correct_answer']]
        answer = st.radio(f"Select the correct answer for Question {i+1}:", options)
        if st.button(f"Submit Answer for Question {i+1}"):
            if answer == question['correct_answer']:
                st.success("Correct!")
            else:
                st.error("Incorrect! The correct answer was " + question['correct_answer'])

if __name__ == "__main__":
    show_quizzes_page()
