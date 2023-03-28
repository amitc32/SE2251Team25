import os
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define API credentials and version
DEVELOPER_KEY = os.environ.get('AIzaSyDfpT5ek6afgYDpTrF61KVlGHYdsJeOzYM') 
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


# Define function to search for a video based on the id and retrieve its statistics
def get_video_info(title):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Searches for the top query and returns video title and id
    request = youtube.search().list(
        part="snippet",
        q=title,
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

    return video_id, video_title, views, likes, comments, score



# Define function to rank a list of videos by popularity
def rank_videos(df):
    ranked_df = df.sort_values(by=['score'], ascending=False)
    ranked_df.reset_index(drop=True, inplace=True)
    return ranked_df

# Song titles should be passed in from billboard api
song_titles = ['Melanie Martinez - DEATH (Official Music Video)', 'ARCANGEL || BZRP Music Sessions #54', "지민 (Jimin) 'Like Crazy' Official MV", 'Ella Baila Sola  - (Video Con Letras) - Eslabon Armado y Peso Pluma - DEL Records 2023', 'Yng Lvcas & Peso Pluma - La Bebe (Remix) [Video Oficial]', 'ROSALÍA, Rauw Alejandro - BESO (Official Video)', 'Toosii - Favorite Song (Official Video)', "Lola Brooke - Don't Play With It (Remix) (Official Video) ft. Latto, Yung Miami", 'DOGTOOTH', "지민 (Jimin) 'Set Me Free Pt.2' Official MV", 'ZAYEL & YoungBoy Never Broke Again - Members Only (music video)', 'Finesse2Tymes - Nobody (feat. Gucci Mane) [Official Music Video]', 'Chino Pacas X Fuerza Regida - Dijeron que no la iba lograr [ Oficial Video ]', 'Maluma, Anuel AA - Diablo, Qué Chimba (Official Video)', 'Rylo Rodriguez - RIGHT HERE (Official Music Video)', "GloRilla, Lil Durk- Ex's (PHATNALL Remix) Official Music Video", 'Finesse2Tymes - Mob Tied [Official Music Video]', 'Lil Nuu - Wicked Inna RaQ 2 (feat. G Herbo) (Official Music Video)', "NLE Choppa - Ain't Gonna Answer Feat. Lil Wayne [Official Video]", 'Fuerza Regida X Eden Muñoz - Y Me Verán [ Oficial Video ]', "Rylo Rodriguez - JA MURANT - 'Sorry Four The Delay' (Mixtape) - 02", 'Juice WRLD - The Light (Official Audio)', '"End Of The World" - Tom MacDonald ft. John Rich', 'Eladio Carrión ft. Bad Bunny - Coco Chanel (Visualizer) | 3MEN2 KBRN', 'EST Gee - THE ONE & ONLY (Official Music Video)', "Rylo Rodriguez - TUBI - 'Sorry Four The Delay' (Mixtape) - 07", 'Fighting Myself [Official Audio] - Linkin Park', 'Miley Cyrus - Flowers (Backyard Sessions)', 'Love You Anyway', 'Ed Sheeran - Eyes Closed [Official Video]']

# Loop through the song titles and get video information for each one
video_data = []
for title in song_titles:
    video_info = get_video_info(title)
    video_data.append(video_info)

# Create a Pandas DataFrame from the video data
columns = ["video_id", "video_title", "views", "likes", "comments", "score"]
df = pd.DataFrame(video_data, columns=columns)

# Sort songs
sorted_songs = rank_videos(df)
print(sorted_songs)