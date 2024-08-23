import streamlit as st
import pages.tutorials as tutorials
import pages.quizzes as quizzes
import pages.forums as forums
from ai.recommender import get_recommendations

# Apply custom CSS
def apply_custom_css():
    st.markdown('<style>' + open('static/css/styles.css').read() + '</style>', unsafe_allow_html=True)

apply_custom_css()

# Main Page Layout
def main():
    st.sidebar.title("EduStream")
    menu = ["Home", "Tutorials", "Quizzes", "Forums", "Personalized Learning"]
    choice = st.sidebar.selectbox("Navigate", menu)

    if choice == "Home":
        show_home_page()
    elif choice == "Tutorials":
        tutorials.show_tutorials_page()
    elif choice == "Quizzes":
        quizzes.show_quizzes_page()
    elif choice == "Forums":
        forums.show_forums_page()
    elif choice == "Personalized Learning":
        show_personalized_learning_page()

def show_home_page():
    st.title("Welcome to EduStream!")
    st.image("static/images/logo.png", use_column_width=True)
    st.markdown("""
        EduStream is your gateway to accessible education. 
        Explore our free and affordable resources tailored for underserved communities.
    """)

def show_personalized_learning_page():
    st.subheader("Your Personalized Learning Path")
    user_data = {"learning_style": "visual", "preferred_topics": ["Math", "Science"]}
    recommendations = get_recommendations(user_data)
    st.write("Based on your preferences, we recommend the following:")
    for rec in recommendations:
        st.write(f"- {rec}")

if __name__ == "__main__":
    main()
