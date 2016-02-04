import urllib
import xml.etree.ElementTree as ET

address = raw_input("Enter location: ")
uh = urllib.urlopen(address)
print 'Retrieving ' + address
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print 'Count: ' + str(len(counts))
total = 0
for item in counts:
    total += int(item.text)
print 'Sum: ' + str(total)