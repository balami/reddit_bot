import requests
import praw

reddit = praw.Reddit(site_name="default_bot", user_agent="<console:poetrybot:1.0>")


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
