import openai
import streamlit as st

# Function to handle OpenAI API errors
def handle_openai_api_error(e):
    st.error(f"An error occurred: {e}")
    return []

# Function to format input data for AI models
def format_user_data(user_data):
    learning_style = user_data.get('learning_style', 'visual')
    preferred_topics = ', '.join(user_data.get('preferred_topics', []))
    return f"Generate learning recommendations for a {learning_style} learner interested in {preferred_topics}."

# Function to interact with OpenAI API
def get_ai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip().split("\n")
    except Exception as e:
        return handle_openai_api_error(e)
