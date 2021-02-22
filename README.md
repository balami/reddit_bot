# Reddit Bot

A reddit bot that posts a random poem as a reply whenever someone mentions "random poem" in the submissions.

## Getting Started

### Prerequisites

Get credentials for a script-type OAuth application from Reddit ```<client_id and client_secret>``` of the app, ```<username, password>``` of the reddit account.
Create a configuration file named ```credentials.ini``` with keys ```client_id, client_secret, username, password``` and put your own crededntials from above as the values.

Now, set up a python virtual environment and then install the dependencies for the app in the venv.
```
pip install -r requirements.txt
```

## Running the application

```
python bot.py
```

Navigate to the reddit account associated with the app. You should see the new posts under the post history. It might take a while for the new post to show up on reddit.

## Built With

* [POEMIST API](https://poemist.github.io/poemist-apidoc/) - POEMIST API to get random poems.
* [PRAW](https://praw.readthedocs.io/en/latest/getting_started/installation.html) - Python Reddit API Wrapper library

## License
This work is licensed under the [GNU General Public License v3.0] - see the [LICENSE](LICENSE) file for details.
