# 1) reverse complete String

inputString = "nikita"
reversedString = ""
i = len(inputString)-1

while i>=0:
    reversedString = reversedString+inputString[i]
    i -= 1

print(reversedString)

