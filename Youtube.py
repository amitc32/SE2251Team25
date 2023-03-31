import os
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from billboardapi import *

# Define API credentials and version
DEVELOPER_KEY = os.environ.get('AIzaSyDfpT5ek6afgYDpTrF61KVlGHYdsJeOzYM') 
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


# Define function to search for a video based on the id and retrieve its statistics
def get_video_info(song):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Searches for the top query and returns video title and id
    request = youtube.search().list(
        part="snippet",
        q=song,
        type="video",
        maxResults=1
    )
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    video_title = response['items'][0]['snippet']['title']

    # Gets stats for music video based on video id
    video_stats = youtube.videos().list(
        part=["statistics"],
        id=video_id
    ).execute()

    views = video_stats['items'][0]['statistics']['viewCount']
    likes = video_stats['items'][0]['statistics']['likeCount']
    comments = video_stats['items'][0]['statistics']['commentCount']

    score = int(views)*0.4 + int(likes)*0.35 + int(comments)*0.25

    return song, video_id, video_title, views, likes, comments, score



# Define function to rank a list of videos by popularity
def rank_videos(df):
    ranked_df = df.sort_values(by=['score'], ascending=False)
    ranked_df.reset_index(drop=True, inplace=True)
    return ranked_df

# Song titles should be passed in from billboard api
song_titles = billboardAPI()
# Loop through the song titles and get video information for each one
video_data = []
for title in song_titles:
    video_info = get_video_info(title)
    video_data.append(video_info)

# Create a Pandas DataFrame from the video data
columns = ["song", "video_id", "video_title", "views", "likes", "comments", "score"]
df = pd.DataFrame(video_data, columns=columns)

# Sort songs
sorted_songs = rank_videos(df)
print(sorted_songs)