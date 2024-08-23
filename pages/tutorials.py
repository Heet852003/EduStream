import streamlit as st
import requests

YOUTUBE_API_KEY = st.secrets["YOUTUBE_API_KEY"]
YOUTUBE_CHANNEL_ID = "khanacademy"

def fetch_youtube_videos(channel_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=5"
    response = requests.get(url).json()
    videos = []
    for item in response['items']:
        if item['id']['kind'] == 'youtube#video':
            videos.append({
                "title": item['snippet']['title'],
                "video_id": item['id']['videoId'],
                "description": item['snippet']['description']
            })
    return videos

def show_tutorials_page():
    st.title("Video Tutorials")
    st.markdown("### Latest Tutorials")

    videos = fetch_youtube_videos(YOUTUBE_CHANNEL_ID, YOUTUBE_API_KEY)
    
    for video in videos:
        st.subheader(video['title'])
        st.video(f"https://www.youtube.com/embed/{video['video_id']}")
        st.write(video['description'])

if __name__ == "__main__":
    show_tutorials_page()
