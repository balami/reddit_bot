from config import config
import requests
import praw

params = config()

# replace the user_agent key's value "poetrybot" by your own app's name, the one created on reddit.
reddit = praw.Reddit(
    client_id=params["client_id"],
    client_secret=params["client_secret"],
    user_agent="<console:poetrybot:1.0>",
    username=params["username"],
    password=params["password"]
)


def get_random_quotes():
    response = requests.get("https://www.poemist.com/api/v1/randompoems")
    return response


subreddit = reddit.subreddit("all")
for submission in subreddit.search(query="poem", time_filter="day", sort="top", limit=10):
    title = submission.title.lower()
    if "poem" in title:
        print(title)
        fn_response = get_random_quotes()
        if fn_response.status_code == 200:
            submission.reply((fn_response.json())[0]['content'])
        break
