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


# 4 ) reverse all other characters except special characters
import re

input = "a@a#1c$d"
rev = ""
expectedOutput = ""
count = 0

# expected output = "d@c#1a$a"
newInput = re.sub("[^a-zA-Z0-9]","",input)

i = len(newInput)-1
while i>=0:
	rev = rev + newInput[i]
	i -= 1
print(rev)

for j in range(len(input)):
	if input[j] in newInput:
		expectedOutput = expectedOutput + rev[count]
		count += 1
	else:
		expectedOutput = expectedOutput + input[j]

print(expectedOutput)






