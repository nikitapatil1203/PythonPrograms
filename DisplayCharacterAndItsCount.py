str1 = "aabbbccaabbb"
# o/p = a2b3c2a2b3

mylist = list(str1)
outputString = ""
count = 1



for i in range(0,len(mylist)-1):
    if mylist[i]==mylist[i+1]:
        count += 1
    else:
        outputString = outputString+mylist[i]+str(count)
        count=1
print(outputString+mylist[-1]+str(count))



