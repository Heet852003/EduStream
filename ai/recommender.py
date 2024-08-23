import openai
import streamlit as st

OPENAI_API_KEY = st.secrets["sk-G1dYqIsLeDbHutqc_raM0UKUwey5QphAD4GqknWQy6T3BlbkFJnSAvfp_vJi6tZ8PhW76tlzwMRrcUBW-bQ0qatEfUMA"]
openai.api_key = OPENAI_API_KEY

def get_recommendations(user_data):
    prompt = f"Generate learning recommendations for a {user_data['learning_style']} learner interested in {', '.join(user_data['preferred_topics'])}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip().split("\n")

if __name__ == "__main__":
    user_data = {"learning_style": "visual", "preferred_topics": ["Math", "Science"]}
    recommendations = get_recommendations(user_data)
    print(recommendations)
