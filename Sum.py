import re

handle = open('C:/Users/jeff.Jeff/OneDrive/Python for EB/regex_sum_166847.txt')
numList = list()

for line in handle:
    line = line.rstrip()
    stuff= re.findall('[0-9]+',line)
    if len(stuff) == 0 : continue
    numList += stuff

lenList = len(numList)
totaled = sum(map(int,numList))

print "There are " + str(lenList) + " values with a sum=" + str(totaled)