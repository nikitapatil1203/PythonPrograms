str1  = "listen"
str2  = "silent"

count1 = {}
count2 = {}

if len(str1) == len(str2):
    for element in str1:
        if element in count1:
            count1[element] += 1
        else:
            count1[element] = 1
    
    for element in str2:
        if element in count2:
            count2[element] +=1
        else:
            count2[element] = 1
    
    if count1 == count2:
        print("Anagram")
    else:
        print("Not Anagram")

else:
    print("Not Anagram")
