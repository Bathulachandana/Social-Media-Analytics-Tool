from datetime import datetime
from collections import defaultdict


def predict_best_instagram_post_time(posts):
    if not posts:
        return "Not enough data"

    hour_engagement = defaultdict(int)
    hour_count = defaultdict(int)

    for post in posts:
        if post["timestamp"]:
            dt = datetime.fromisoformat(post["timestamp"].replace("Z", "+00:00"))
            hour = dt.hour

            hour_engagement[hour] += post["engagement"]
            hour_count[hour] += 1

    avg_engagement = {}

    for hour in hour_engagement:
        avg_engagement[hour] = hour_engagement[hour] / hour_count[hour]

    best_hour = max(avg_engagement, key=avg_engagement.get)

    return f"{best_hour}:00"
