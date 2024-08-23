import openai
import streamlit as st

# Ensure you have your OpenAI API key stored in Streamlit Secrets
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

def get_recommendations(user_data):
    prompt = f"Generate learning recommendations for a {user_data['learning_style']} learner interested in {', '.join(user_data['preferred_topics'])}."

    # Use the correct API method based on the latest OpenAI version
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the generated text
        recommendations = response['choices'][0]['message']['content'].strip().split("\n")
        return recommendations
    
    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
        return []

if __name__ == "__main__":
    # Test the function
    user_data = {"learning_style": "visual", "preferred_topics": ["Math", "Science"]}
    recommendations = get_recommendations(user_data)
    print(recommendations)
