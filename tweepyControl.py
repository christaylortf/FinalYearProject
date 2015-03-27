import tweepy
import urllib3
urllib3.disable_warnings()


consumer_key = 'yZA8ABXinV6rQlICV3DNyKwHV'
consumer_secret = 'D1xMDf3NnDCcYtu5KRcwes8MzQbAWW4pPQHEYL2tHH0T70L9E1'
access_token = '1731498314-nPqsTsliicuwDmeBnZplnyM0ZYXR3TAnArZPhdR'
access_token_secret = '1Tu4TYpL5ASLOzAFBDqWH721ETxVJUdT8hKnczSLyvWcH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def showTweetText(tweetID):
	status = api.get_status(tweetID)
	print status.text
	
def showTweetAuthor(tweetID):
	urllib3.disable_warnings()
	tweet = api.get_status(tweetID)
	user = tweet.user.screen_name
	print "The author of that tweet is: @"+user
	
def showTimeCreated(tweetID):
	tweet = api.get_status(tweetID)
	timeCreated = tweet.created_at
	print 'Tweet was created at:'
	print timeCreated

def testingMethod(tweetID)
	tweet = api.get_status(tweetID)
	