import random

def mock_get_recommendations(user_data):
    topics = user_data['preferred_topics']
    learning_style = user_data['learning_style']
    
    recommendations = [
        f"{random.choice(['Watch', 'Study', 'Practice'])} {topic} using {learning_style} aids"
        for topic in topics
    ]
    
    return recommendations

def get_recommendations(user_data):
    return mock_get_recommendations(user_data)

if __name__ == "__main__":
    user_data = {"learning_style": "visual", "preferred_topics": ["Math", "Science"]}
    recommendations = get_recommendations(user_data)
    print(recommendations)
