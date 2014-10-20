import time
import urllib2
from BeautifulSoup import *
# from bs4 import *


print 'Welcome to the Get Twitter tool. This tool will allow you to download a page from Twitter to be used to extract the data.'

print "Current date & time {}".format(time.strftime("%c"))
userResponse = raw_input("Please enter the full URL from the Tweet page: ")
response = urllib2.urlopen(userResponse)
html = response.read()

soup = BeautifulSoup(html)
with open(time.strftime("%c"), 'a') as f:
	f.write(html)
