import requests

GRAPH_URL = "https://graph.facebook.com/v18.0"


def get_user_pages(access_token):
    url = f"{GRAPH_URL}/me/accounts"
    params = {
        "access_token": access_token
    }
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()["data"]


def get_page_info(page_id, page_token):
    url = f"{GRAPH_URL}/{page_id}"
    params = {
        "fields": "name,followers_count,fan_count",
        "access_token": page_token
    }

    r = requests.get(url, params=params)
    print("PAGE INFO RAW:", r.text)   # debug
    r.raise_for_status()
    return r.json()


# ✅ ADD THIS FUNCTION BELOW
def get_page_insights(page_id, page_token):
    metrics = "page_impressions,page_engaged_users"

    url = f"{GRAPH_URL}/{page_id}/insights"
    params = {
        "metric": metrics,
        "period": "week",
        "access_token": page_token
    }

    r = requests.get(url, params=params)

    print("INSIGHTS RAW:", r.text)  # debug

    if r.status_code != 200:
        return {}

    insights = {}
    data = r.json().get("data", [])

    for item in data:
        if item.get("values"):
            insights[item["name"]] = item["values"][0]["value"]

    return insights



def get_page_posts(page_id, page_token):
    url = f"{GRAPH_URL}/{page_id}/posts"
    params = {
        "fields": "message,created_time,likes.summary(true),comments.summary(true)",
        "access_token": page_token
    }

    r = requests.get(url, params=params)
    r.raise_for_status()

    posts_data = r.json()["data"]

    posts = []

    for post in posts_data:
        posts.append({
            "message": post.get("message", "No text"),
            "created_time": post.get("created_time"),
            "likes": post.get("likes", {}).get("summary", {}).get("total_count", 0),
            "comments": post.get("comments", {}).get("summary", {}).get("total_count", 0)
        })

    return posts
