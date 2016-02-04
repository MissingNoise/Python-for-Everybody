import urllib
from bs4 import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('span')
i = 0
for tag in tags:
    i += int(tag.contents[0])
    
print i