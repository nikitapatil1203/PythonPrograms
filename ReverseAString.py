# 1) reverse complete String

inputString = "nikita"
reversedString = ""
i = len(inputString)-1

while i>=0:
    reversedString = reversedString+inputString[i]
    i -= 1

print(reversedString)



# 2) reverse only words not characters
inputString = "Hello, World! Welcome to Python.".split(" ")
reversedString = ""
i = len(inputString)-1

while i>=0:
    reversedString = reversedString + inputString[i] + " "
    i -= 1

print(reversedString.strip())

