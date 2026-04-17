import requests

HEADERS = {
    "Accept": "application/vnd.github+json"
}

def get_github_user(username):
    try:
        url = f"https://api.github.com/users/{username}"
        r = requests.get(url, headers=HEADERS)

        if r.status_code != 200:
            print("GitHub user error:", r.text)
            return None

        data = r.json()

        return {
            "username": data.get("login"),
            "followers": data.get("followers"),
            "following": data.get("following"),
            "public_repos": data.get("public_repos")
        }

    except Exception as e:
        print("GitHub user exception:", e)
        return None


def get_github_repos(username):
    try:
        url = f"https://api.github.com/users/{username}/repos"
        r = requests.get(url, headers=HEADERS)

        if r.status_code != 200:
            print("GitHub repos error:", r.text)
            return []

        repos = r.json()

        repo_list = []
        for repo in repos:
            repo_list.append({
                "name": repo.get("name"),
                "stars": repo.get("stargazers_count", 0),
                "forks": repo.get("forks_count", 0),
                "watchers": repo.get("watchers_count", 0),
                "open_issues": repo.get("open_issues_count", 0),
                "language": repo.get("language")
            })

        return repo_list

    except Exception as e:
        print("GitHub repos exception:", e)
        return []
