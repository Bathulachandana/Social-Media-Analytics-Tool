import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_best_post_time(videos):
    if not videos or len(videos) < 3:
        return "Not enough data for ML prediction"

    data = []

    for v in videos:
        data.append({
            "day": v["published"].weekday(),
            "hour": v["published"].hour,
            "views": v["views"]
        })

    df = pd.DataFrame(data)

    X = df[["day", "hour"]]
    y = df["views"]

    model = LinearRegression()
    model.fit(X, y)

    best_score = -1
    best_time = None

    for day in range(7):
        for hour in range(24):
            pred = model.predict([[day, hour]])[0]
            if pred > best_score:
                best_score = pred
                best_time = (day, hour)

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return f"{days[best_time[0]]} at {best_time[1]}:00"
