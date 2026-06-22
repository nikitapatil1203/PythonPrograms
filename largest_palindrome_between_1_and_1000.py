
firstHighestNum = 100
secondHighestNum = 100
highestPalindrome = 1

for i in range(100,1000):
    for j in range(100, 1000):
        reverseOfNum = 0
        mulOfNumbers = i*j
        product = mulOfNumbers
        while (mulOfNumbers > 0):
            reverseOfNum = reverseOfNum * 10 + mulOfNumbers % 10
            mulOfNumbers = mulOfNumbers // 10

        if(reverseOfNum == product) and (highestPalindrome < reverseOfNum):
            firstHighestNum = i
            secondHighestNum = j
            highestPalindrome = reverseOfNum

print("firstHighestNum is : "+str(firstHighestNum))
print("secondHighestNum is : "+str(secondHighestNum))
