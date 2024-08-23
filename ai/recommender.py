import openai
import streamlit as st

# Ensure you have your OpenAI API key stored in Streamlit Secrets
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

def get_recommendations(user_data):
    prompt = f"Generate learning recommendations for a {user_data['learning_style']} learner interested in {', '.join(user_data['preferred_topics'])}."

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Use the correct model
            prompt=prompt,
            max_tokens=150,  # Limit the number of tokens for the response
        )

        # Extract the generated text
        recommendations = response.choices[0].text.strip().split("\n")
        return recommendations

    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
        return []

def show_personalized_learning_page():
    st.subheader("Your Personalized Learning Path")
    user_data = {"learning_style": "visual", "preferred_topics": ["Math", "Science"]}
    recommendations = get_recommendations(user_data)

    if recommendations:
        st.write("Based on your preferences, we recommend the following:")
        for rec in recommendations:
            st.write(f"- {rec}")

if __name__ == "__main__":
    show_personalized_learning_page()
