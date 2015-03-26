import tweepy

consumer_key = 'yZA8ABXinV6rQlICV3DNyKwHV'
consumer_secret = 'D1xMDf3NnDCcYtu5KRcwes8MzQbAWW4pPQHEYL2tHH0T70L9E1'
access_token = '1731498314-nPqsTsliicuwDmeBnZplnyM0ZYXR3TAnArZPhdR'
access_token_secret = '1Tu4TYpL5ASLOzAFBDqWH721ETxVJUdT8hKnczSLyvWcH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('ChrisTaylor_TSA')
print user.screen_name
print user.followers_count
for friend in user.friends():
   print friend.screen_name