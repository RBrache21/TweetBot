import tweepy
import time

auth = tweepy.OAuthHandler('zLjyd1t2kFoFpnMdyBso1hOFm', 'DAQoWTO125IKb9CfNyDNg6b0IlYq294HswzUGooRyAAB4iWoaQ')
auth.set_access_token('212309472-MW3wi06GMMGwikdVtu0SZNEPYoJyZ37sJ6XwCDUY',
                      'Yet17kQjzKOMyLPBO9DLF1QNQYT1JY09Dg97P1Ssrs3B5')

api = tweepy.API(auth)

user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# bot that likes specified posts
search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepyError as e:
        print(e.reason)
    except StopIteration:
        break

# bot that follows specified people
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'xXFez_2k':
#         follower.follow()
#         break
