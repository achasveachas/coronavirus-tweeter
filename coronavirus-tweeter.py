from os import environ
import tweepy

from coronavirus import VIRUS_TWEETS

twitter_api_key = environ['twitter_api_key']
twitter_api_secret = environ['twitter_api_secret']
twitter_access_token = environ['twitter_access_token']
twitter_access_secret = environ['twitter_access_secret']
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)
twitter_client = tweepy.API(auth)

reply_to = ""

for idx, tweet in enumerate(VIRUS_TWEETS):
    latest_tweet = twitter_client.update_status(
        status=tweet,
        in_reply_to_status_id=reply_to,
        auto_populate_reply_metadata=True,
    )
    reply_to = latest_tweet.id_str
    print(f"Sending Tweet #{idx + 1}")