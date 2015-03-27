from tweepyControl import *

print "Welcome to the Twitter Forensic Storage Tool"
tweetID = raw_input("Enter the ID of the Tweet to investigate")

print '\n \n== Menu =='
print '1. Enter tweet ID'
if tweetID!="":
	print '2. View Tweet Text'
	print '3. View Tweet Author'

menuChoice = input("Please choose an option: ")

if menuChoice == 2:
	print 'Showing Tweet Text'
	showTweetText(tweetID)
else:
	print 'Oh oh!'

