lst = []
while len(lst) < 3:
    NewNum = input('Enter a number: ')
    if type(NewNum) == int:
        lst.append(NewNum)
    
print sorted(lst)