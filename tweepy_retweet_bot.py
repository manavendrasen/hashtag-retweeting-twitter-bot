import tweepy
import time

# your keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# hashtag to retweet
search = "ReduceNiftSemesterFees"

nr = 500
count = 0
for tweet in tweepy.Cursor(api.search, search).items(nr):
    try:
        count += 1
        print(str(count)+'. Liked: ' + tweet.text)
        tweet.favorite()
        tweet.retweet()
        # time delay
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break