from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build(
    serviceName="youtube",
    version="v3",
    developerKey=API_KEY
)

def get_video_stats(video_id):
    request = youtube.videos().list(
        part="statistics,snippet",
        id=video_id
    )
    response = request.execute()

    if not response["items"]:
        return None

    data = response["items"][0]

    stats = data["statistics"]
    snippet = data["snippet"]

    return {
        "title": snippet["title"],
        "views": int(stats.get("viewCount", 0)),
        "likes": int(stats.get("likeCount", 0)),
        "comments": int(stats.get("commentCount", 0))
    }
