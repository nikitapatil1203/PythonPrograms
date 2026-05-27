str1 = "aabbbccaabbb"
# o/p = a2b3c2a2b3

mylist = list(str1)
outputString = ""
count = 1



for i in range(0,len(mylist)-1):
    if mylist[i]==mylist[i+1]:
        counter += 1
    else:
        ab = ab+mylist[i]+str(counter)
        counter=1
print(ab+mylist[i]+str(counter))



