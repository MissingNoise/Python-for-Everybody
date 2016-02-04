name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    count[words[1]] = count.get(words[1], 0) + 1

    
bigword = None
bignumber = None

for word,number in count.items():
    if bignumber is None or number > bignumber:
        bigword = word
        bignumber = number
        
print bigword, bignumber