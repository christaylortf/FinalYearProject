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
	
	tweet = api.get_status(tweetID)
	user = tweet.user.screen_name
	print "The author of that tweet is: @"+user
	
def showTimeCreated(tweetID):
	tweet = api.get_status(tweetID)
	timeCreated = tweet.created_at
	print 'Tweet was created at:'
	print timeCreated

def beenRetweeted(tweetID):
	tweet = api.get_status(tweetID)
	if tweet.retweet:
		print 'This tweet has been retweeted at least once'
	else:
		print 'This tweet has not been retweeted'
		
def beenFavd(tweetID):
	tweet = api.get_status(tweetID)
	if tweet.favorited:
		print 'This tweet has been favourited at least once'
	else:
		print 'This tweet has not been favourited'

def showLocation(tweetID):
	tweet = api.get_status(tweetID)
	location = tweet.user.location.encode('utf8')
	if location != "":
		print location
	else:
		print 'This tweet does not have a location assigned to it'
		
def showUserTimezone(tweetID):
	tweet = api.get_status(tweetID)
	print "Time-zone:", tweet.user.time_zone
	
def getUserCoordinates(tweetID):
	tweet = api.get_status(tweetID)
	for key,value in tweet.geo.items():
		if key == 'coordinates':
			return value
				
def showUserCoordinates(tweetID):
	print getUserCoordinates(tweetID)

def showUserMap(tweetID):
	coords = getUserCoordinates(tweetID)
	print coords
	coords1 = str(coords[:-1])
	coords1 = coords1[1:-1]

	coords2 = str(coords[1:])
	coords2 = coords2[1:-1]
	print coords1
	print coords2
	
	import webbrowser
	toOpen = "https://www.google.co.uk/maps/search/"+coords1+","+coords2
	webbrowser.open(toOpen)
	
def getHashtags(tweetID):
	tweet = api.get_status(tweetID)
	print tweet.entities.get('hashtags')

def testingMethod(tweetID):
	import time
	tweet = api.get_status(tweetID)
	ids = [tweet.user.screen_name]
	for page in tweepy.Cursor(api.followers_ids, screen_name="@"+tweet.user.screen_name+"").pages():
		ids.extend(page)
		time.sleep(60)
		
	screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids)]
	print screen_names