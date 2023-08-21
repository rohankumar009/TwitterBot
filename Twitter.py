import tweepy
import os

# Twitter API keys and tokens
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Post URL of the tweet you want to interact with
tweet_url = "https://twitter.com/username/status/tweet_id"

# Extract tweet ID from the URL
tweet_id = tweet_url.split("/")[-1]

# Get the tweet and its replies
tweet = api.get_status(tweet_id, tweet_mode="extended")
replies = tweepy.Cursor(api.search, q=f"to:{tweet.user.screen_name}", since_id=tweet.id_str).items()

# Like the comments
for reply in replies:
    if reply.in_reply_to_status_id == tweet.id:
        api.create_favorite(reply.id)
        print(f"Liked comment: {reply.full_text}")

