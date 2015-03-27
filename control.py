from tweepyControl import *
import sys

def showMenu():
	print '\n \n== Menu =='
	print '1. Enter tweet ID'
	if tweetID!="":
		print '2. View Tweet Text'
		print '3. View Tweet Author'
		print '0 to quit'
	menuChoice = input("\nPlease choose an option: ")
	menuAction(menuChoice)
	
def menuAction(menuChoice):
	if menuChoice == 1:
		tweetID = raw_input("Enter the ID of the new Tweet to investigate")
		print "Your working TweetID is: "+tweetID
		showMenu()
	elif menuChoice == 2:
		showTweetText(tweetID)
		showMenu()
	elif menuChoice == 3:
		showTweetAuthor(tweetID)
		showMenu()
	elif menuChoice == 0:
		sys.exit()
	else:
		print 'Oh oh! That menu item isn\t available. Please try again.'
		showMenu()


print "Welcome to the Twitter Forensic Storage Tool"
tweetID = raw_input("Enter the ID of the Tweet to investigate")
showMenu()



