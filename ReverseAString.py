# 1) reverse complete String

inputString = "nikita"
reversedString = ""
i = len(inputString)-1

while i>=0:
    reversedString = reversedString+inputString[i]
    i -= 1

print(reversedString)


##############################################################


# 2) reverse only words not characters
inputString = "Hello, World! Welcome to Python.".split(" ")
reversedString = ""
i = len(inputString)-1

while i>=0:
    reversedString = reversedString + inputString[i] + " "
    i -= 1

print(reversedString.strip())



#############################################################



# 3) reverse whole string as well as each word from a string
inputString = "nikita patil is my name".split(" ")
reversedString = ""

i = len(inputString) - 1

while i >= 0:
    newString = inputString[i]
    j = len(inputString[i]) - 1

    while j >= 0:
        reversedString = reversedString + newString[j]
        j -= 1

    reversedString = reversedString + " "
    i -= 1

print(reversedString.strip())



##########################################################






