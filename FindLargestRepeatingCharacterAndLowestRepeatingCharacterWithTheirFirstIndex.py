name = "automatiionnnn"
newList = list(name)
freq_map = {}


mostRepeatingCharacterCount = 0
leastRepeatedCharacterCount = len(name)
mostRepeatingCharacter = None
leastRepeatedCharacter = None

for i in newList:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i] = 1


for key, value in freq_map.items():
    if mostRepeatingCharacterCount < value:
        mostRepeatingCharacterCount = value
        mostRepeatingCharacter = key

    if leastRepeatedCharacterCount > value:
        leastRepeatedCharacterCount = value
        leastRepeatedCharacter = key

print("mostRepeatingCharacterCount : "+str(mostRepeatingCharacterCount))
print("mostRepeatingCharacter : "+mostRepeatingCharacter)
print("leastRepeatedCharacterCount : "+str(leastRepeatedCharacterCount))
print("leastRepeatedCharacter : "+leastRepeatedCharacter)
















