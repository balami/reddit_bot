# Reddit Bot

A reddit bot that posts a random poem as a reply whenever someone mentions poem in the submissions.


## Getting Started

### Prerequisites

Get credentials for a script-type OAuth application from Reddit ```<client_id and client_secret>``` of the app, ```<username, password>``` of the reddit account.

Create a PRAW INI file for storing app credentials. Give a site name and list the key value pairs for each: ```client_id, client_secret, username, password```.
Also add user_agent values for your bot app ```script:%(bot_name)s:v%(bot_version)s (by u/%(bot_author)s)```

Install [Docker](https://www.docker.com/get-started) and run the following command.
```
docker-compose build
```
After the image is built successfully, run the docker container.

## Running the application

```
docker-compose up
```

Navigate to the reddit account associated with the app. You should see the new posts under the post history. It might take a while for the new post to show up on reddit.

## Built With

* [POEMIST API](https://poemist.github.io/poemist-apidoc/) - POEMIST API to get random poems.
* [PRAW](https://praw.readthedocs.io/en/latest/getting_started/installation.html) - Python Reddit API Wrapper library
* [Docker](https://docs.docker.com/engine/install/ubuntu/) - Docker Engine on Ubuntu

## License
This work is licensed under the [GNU General Public License v3.0] - see the [LICENSE](LICENSE) file for details.
