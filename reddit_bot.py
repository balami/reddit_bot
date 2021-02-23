import requests
import praw


def praw_config():
    """
    Pass app params from PRAW INI file to instantiate. Replace the site_name value by your own site name.
    """
    r = praw.Reddit(site_name="default_bot", config_interpolation="basic")
    return r


def get_random_quotes():
    """
    Get random poems from the POEMIST API.
    """
    response = requests.get("https://www.poemist.com/api/v1/randompoems")
    return response


def post_reply(reddit):
    """Pass the search query and if a submission contains the word and is not already replied, post a poem as a reply.
    """
    subreddit = reddit.subreddit("all")
    already_replied = []

    # The params time_filter, sort and limit are optional.
    for submission in subreddit.search(query="poem", time_filter="week", sort="top", limit=50):
        title = submission.title.lower()
        if "poem" in title and submission.id not in already_replied:
            fn_response = get_random_quotes()
            # only continue if the API call to POEMIST was successful.
            if fn_response.status_code == 200:
                # reply to the submission
                submission.reply((fn_response.json())[0]['content'])
                # store the submission ID so that we don't reply again
                already_replied.append(submission.id)
                # to the same submission.


if __name__ == "__main__":
    reddit_config = praw_config()
    post_reply(reddit_config)
