import openai
import streamlit as st

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

def get_recommendations(user_data):
    prompt = f"Generate learning recommendations for a {user_data['learning_style']} learner interested in {', '.join(user_data['preferred_topics'])}."
    
    response = openai.Completion.create(
        engine="text-curie-001",  # Using text-curie-001 model
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    return response.choices[0].text.strip().split("\n")

if __name__ == "__main__":
    user_data = {"learning_style": "visual", "preferred_topics": ["Math", "Science"]}
    recommendations = get_recommendations(user_data)
    print(recommendations)
