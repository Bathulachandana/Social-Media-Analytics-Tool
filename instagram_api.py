import requests
from datetime import datetime

BASE_URL = "https://graph.facebook.com/v19.0"


# -------------------------------
# Get Instagram Business ID
# -------------------------------
def get_instagram_business_id(page_id, token):
    url = f"{BASE_URL}/{page_id}"
    params = {
        "fields": "instagram_business_account",
        "access_token": token
    }

    res = requests.get(url, params=params).json()

    if "instagram_business_account" in res:
        return res["instagram_business_account"]["id"]

    return None


# -------------------------------
# Get Account Insights
# -------------------------------
def get_instagram_insights(ig_id, token):

    data = {}

    # Reach
    reach = requests.get(
        f"{BASE_URL}/{ig_id}/insights",
        params={
            "metric": "reach",
            "period": "day",
            "access_token": token
        }
    ).json()

    data["reach"] = (
        reach["data"][0]["values"][0]["value"]
        if "data" in reach and reach["data"]
        else 0
    )

    # Followers
    followers = requests.get(
        f"{BASE_URL}/{ig_id}",
        params={
            "fields": "followers_count",
            "access_token": token
        }
    ).json()

    data["followers"] = followers.get("followers_count", 0)

    # Profile Views
    profile = requests.get(
        f"{BASE_URL}/{ig_id}/insights",
        params={
            "metric": "profile_views",
            "period": "day",
            "access_token": token
        }
    ).json()

    data["profile_views"] = (
        profile["data"][0]["values"][0]["value"]
        if "data" in profile and profile["data"]
        else 0
    )

    return data


# -------------------------------
# Get Media
# -------------------------------
def get_instagram_media_insights(ig_id, token):

    url = f"{BASE_URL}/{ig_id}/media"

    params = {
        "fields": "id,caption,like_count,comments_count,timestamp",
        "access_token": token
    }

    response = requests.get(url, params=params)

    data = response.json()

    media_list = []

    if "data" in data:
        for item in data["data"]:
            media_list.append({
                "id": item.get("id"),
                "caption": item.get("caption", "No caption"),
                "likes": item.get("like_count", 0),
                "comments": item.get("comments_count", 0),
                "timestamp": item.get("timestamp")
            })

    return media_list

