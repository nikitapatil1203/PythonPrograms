numlist = [1,10,3,5,6,9]
numlist.sort()
newString = []

for i in range(1,numlist[len(numlist)-1]):
    newString.append(i)
    i+=1

newString.append(i)
print(newString)




