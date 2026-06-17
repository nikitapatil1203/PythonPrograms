numList = [20,15,8,2,12,5]
numList.sort()
smallestDiff = numList[len(numList)-1]
print(smallestDiff)
pair = []


for i in range(0, len(numList)):
    for j in range(i+1, len(numList)):
        difference = abs(numList[i] - numList[j])
        if smallestDiff > difference:
            smallestDiff = difference
            pair = [(numList[i], numList[j])]

        elif smallestDiff == difference:
            pair.append((numList[i],numList[j]))

print(smallestDiff)
print(pair)

