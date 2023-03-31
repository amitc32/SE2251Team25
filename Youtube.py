import os
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import billboardapi as bbd

class Youtube():
    # Define API credentials and version
    DEVELOPER_KEY = os.environ.get('AIzaSyDfpT5ek6afgYDpTrF61KVlGHYdsJeOzYM') 
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Define function to search for a video based on the id and retrieve its statistics
    def get_video_info(title):
        # Searches for the top query and returns video title and id
        request = Youtube.youtube.search().list(
        part="snippet",
        q=title,
        type="video",
        maxResults=1
        )
        response = request.execute()
        video_id = response['items'][0]['id']['videoId']
        video_title = response['items'][0]['snippet']['title']

        # Gets stats for music video based on video id
        video_stats = Youtube.youtube.videos().list(part=["statistics"], id=video_id).execute()

        views = video_stats['items'][0]['statistics']['viewCount']
        likes = video_stats['items'][0]['statistics']['likeCount']
        comments = video_stats['items'][0]['statistics']['commentCount']

        score = int(views)*0.4 + int(likes)*0.35 + int(comments)*0.25

        return video_id, video_title, views, likes, comments, score
    

    # Define function to rank a list of videos by popularity
    def rank_videos():
        ranked_df = Youtube.sort_videos.sort_values(by=['score'], ascending=False)
        ranked_df.reset_index(drop=True, inplace=True)
        return ranked_df
    
    def sort_videos():
        # Song titles should be passed in from billboard api
        song_titles = bbd.billboard.run()
        # Loop through the song titles and get video information for each one
        video_data = []
        for title in song_titles:
            song_name  = title.split(" AND ")
            video_info = Youtube.get_video_info(song_name[1])
            video_data.append(video_info)

        # Create a Pandas DataFrame from the video data
        columns = ["video_id", "video_title", "views", "likes", "comments", "score"]
        return pd.DataFrame(video_data, columns=columns)

        # Sort songs
    def sorted_songs():
        return Youtube.rank_videos()
