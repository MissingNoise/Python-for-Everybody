# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from bs4 import *

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
position = raw_input('Enter position: ')
count = int(count)
print "Retrieving: " + url
def pos():
    global url
    p = int(position)
    for tag in tags:
        p -= 1
        n = tag.get('href', None)
        if p != 0: continue
        print "Retrieving: " + n
        url = n
while count > 0:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    pos()
    count -= 1