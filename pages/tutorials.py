import streamlit as st
import requests

# Fetch YouTube videos using YouTube Data API
def fetch_youtube_videos(channel_id, api_key):
    try:
        url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=5"
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        # Check if 'items' exists in the response
        if 'items' in data:
            videos = []
            for item in data['items']:
                if item['id']['kind'] == 'youtube#video':
                    videos.append({
                        "title": item['snippet']['title'],
                        "video_id": item['id']['videoId'],
                        "description": item['snippet']['description']
                    })
            return videos
        else:
            st.error("Unexpected response format from the YouTube API. Please try again later.")
            return []

    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            st.error("Access to the YouTube API was denied. Please check your API key.")
        elif response.status_code == 429:
            st.error("Too many requests to the YouTube API. Please try again later.")
        elif response.status_code == 400:
            st.error("Bad Request. Please check the channel ID and API key.")
        else:
            st.error(f"Failed to fetch videos: {e}")
        return []

    except Exception as e:
        st.error("An unexpected error occurred. Please try again later.")
        return []

def show_tutorials_page():
    st.title("Video Tutorials")
    st.markdown("### Latest Tutorials")

    # Replace with your YouTube API key and a known valid channel ID for testing
    YOUTUBE_API_KEY = st.secrets["YOUTUBE_API_KEY"]
    YOUTUBE_CHANNEL_ID = "UC4a-Gbdw7vOaccHmFo40b9g"  # Known valid Channel ID for Khan Academy

    videos = fetch_youtube_videos(YOUTUBE_CHANNEL_ID, YOUTUBE_API_KEY)

    if videos:
        for video in videos:
            st.subheader(video['title'])
            st.video(f"https://www.youtube.com/embed/{video['video_id']}")
            st.write(video['description'])
    else:
        st.warning("No videos available at the moment.")

if __name__ == "__main__":
    show_tutorials_page()
