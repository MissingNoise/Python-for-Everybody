import urllib
import json
address = raw_input("Enter location: ")
uh = urllib.urlopen(address)
print 'Retrieving ' + address
data = uh.read()
print 'Retrieved',len(data),'characters'
js = json.loads(str(data))
count = 0
totsum = 0
for item in js["comments"]:
    count += 1
    totsum += item["count"]
    
print "Count:", count
print "Sum:", totsum
