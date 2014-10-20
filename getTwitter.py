import urllib2
from BeautifulSoup import *

print 'Welcome to the Get Twitter tool. This tool will allow you to download a page from Twitter to be used to extract the data'

userResponse = raw_input("Please enter the full URL from the Tweet page")
response = urllib2.urlopen(userResponse)
html = response.read()

soup = BeautifulSoup(html)

print(soup.prettify())
