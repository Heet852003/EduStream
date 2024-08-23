import requests
import pandas as pd

# Function to fetch data from an API
def fetch_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

# Function to load a CSV file into a DataFrame
def load_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise Exception(f"Error loading CSV file: {e}")

# Function to process YouTube video data
def process_youtube_data(videos):
    processed_videos = []
    for video in videos:
        processed_videos.append({
            "title": video['snippet']['title'],
            "video_id": video['id']['videoId'],
            "description": video['snippet']['description']
        })
    return processed_videos
