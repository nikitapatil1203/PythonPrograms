str1 = "aabbbccaabbb"
# o/p = a2b3c2a2b3

mylist = list(str1)
outputString = ""
count = 1



for i in range(0,len(list1)-1):
    if list1[i]==list1[i+1]:
        counter += 1
    else:
        ab = ab+list1[i]+str(counter)
        counter=1
print(ab+list1[i]+str(counter))



