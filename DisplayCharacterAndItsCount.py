str1 = "aabbbccaabbb"
# o/p = a2b3c2a2b3

mylist = list(str1)
outputString = mylist[0]
count = 1


for i in range(1, len(mylist)):
    if mylist[i] == mylist[i-1]:
        count += 1
    else:
        outputString = outputString + str(count) + mylist[i]
        count =1

print(outputString+str(count))



