numlist = [1,10,3,5,6,9]
numlist.sort()
a = 0
newString = []

for i in range(1,numlist[-1]+1):
    if i in numlist:
        newString.append(numlist[a])
        a += 1
    else:
        newString.append(i)

print(newString)



