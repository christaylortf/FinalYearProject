import time
import urllib2
from BeautifulSoup import *
# from bs4 import *
import hashlib

print 'Welcome to the Get Twitter tool. This tool will allow you to download a page from Twitter to be used to extract the data.'

print "Current date & time {}".format(time.strftime("%c"))
userResponse = raw_input("Please enter the full URL from the Tweet page: ")
response = urllib2.urlopen(userResponse)
html = response.read()

fileTime = time.strftime("%c")
soup = BeautifulSoup(html)
with open(fileTime, 'a') as f:
	f.write(html)

hasher = hashlib.md5()
with open(fileTime, 'rb') as afile:
	buf = afile.read()
	hasher.update(buf)
print(hasher.hexdigest())

with open('hashValues','a') as f:
	f.write(fileTime + " - " + hasher.hexdigest() + "\n")
