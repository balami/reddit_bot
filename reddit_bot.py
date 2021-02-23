import requests
import praw

'''
Pass app params from PRAW INI file to instantiate. Replace the site_name value by your own site name.
'''
reddit = praw.Reddit(site_name="default_bot", config_interpolation="basic")

'''
Function to get random poems from the POEMIST API. The call response is a json with 5 items.
'''


def get_random_quotes():
    response = requests.get("https://www.poemist.com/api/v1/randompoems")
    return response


'''Pass the subreddit name as the param to the method. 
To check if we already replied, instantiate an empty list to store submission IDs which are unique for all submissions.
 '''

subreddit = reddit.subreddit("all")
already_replied = []

'''Pass the search string and other optional parameters like sorting by top submissions, limiting the result to only n 
number, showing search results only from within 24 hour and so on'''

for submission in subreddit.search(query="poem", time_filter="day", sort="top", limit=10):
    title = submission.title.lower()
    if "poem" in title and submission.id not in already_replied:
        fn_response = get_random_quotes()
        if fn_response.status_code == 200:  # only continue if the API call to POEMIST was successful.
            submission.reply((fn_response.json())[0]['content'])  # reply to the submission
            already_replied.append(submission.id)  # store the submission ID so that we don't reply again
            # to the same submission.
        break
