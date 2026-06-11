numList = [20,15,8,2,12,5]
numList.sort()
smallestdiff = numList[len(numList)-1]
print(smallestdiff)
pair = []


for i in range(0, len(numList)-1):
    for j in range(i+1, len(numList)-1):
        difference = abs(numList[i] - numList[j])
        if smallestdiff > difference:
            smallestdiff = difference
            pair = [(numList[i], numList[j])]

        elif smallestdiff == difference:
            pair.append((numList[i],numList[j]))

print( smallestdiff)
print(pair)

