numList = [2,44,5,1,6,44,0,76,90,4,-3,77]
smallestNum = numList[0]

for num in numList:
    if num < smallestNum:
        smallestNum = num

print(smallestNum)
