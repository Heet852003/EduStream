import openai
import streamlit as st

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

def get_recommendations(user_data):
    prompt = f"Generate learning recommendations for a {user_data['learning_style']} learner interested in {', '.join(user_data['preferred_topics'])}."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # This uses the ChatGPT model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the response text
    recommendations = response['choices'][0]['message']['content'].strip().split("\n")
    return recommendations

if __name__ == "__main__":
    user_data = {"learning_style": "visual", "preferred_topics": ["Math", "Science"]}
    recommendations = get_recommendations(user_data)
    print(recommendations)
