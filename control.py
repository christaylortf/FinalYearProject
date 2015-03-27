from tweepyControl import *
import sys

def showMenu():
	print '\n \n== Menu =='
	print '1. Enter tweet ID'
	if tweetID!="":
		print '2. View Tweet Text'
		print '3. View Tweet Author'
		print '4. View time created'
		print '5. Has this tweet been retweeted?'
		print '6. Has this tweet been favorited?'
		print '7. Show user location'
		print '	7.1 Show location coordinated'
		print '	7.2  Show user timezone'
		print '999 for test method'
	print '0 to quit'
	menuChoice = input("\nPlease choose an option: ")
	menuAction(menuChoice)
	
def menuAction(menuChoice):
	global tweetID
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
	elif menuChoice == 4:
		showTimeCreated(tweetID)
		showMenu()
	elif menuChoice == 5:
		beenRetweeted(tweetID)
		showMenu()
	elif menuChoice == 6:
		beenFavd(tweetID)
		showMenu()
	elif menuChoice == 7:
		showLocation(tweetID)
		showMenu()
	elif menuChoice == 7.1:
		showUserCoordinates(tweetID)
		showMenu()
	elif menuChoice == 7.2:
		showUserTimezone(tweetID)
		showMenu()
	elif menuChoice == 0:
		print 'Goodbye!'
		sys.exit()
	elif menuChoice == 999:
		testingMethod(tweetID)
		showMenu()
	else:
		print 'Oh oh! That menu item isn\t available. Please try again.'
		showMenu()


print "Welcome to the Twitter Forensic Storage Tool"
global tweetID 
tweetID = raw_input("Enter the ID of the Tweet to investigate: ")
showMenu()



