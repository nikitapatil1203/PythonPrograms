input = "anviaj"
newString = ""

for i in range(len(input)):
    output = ""
    for j in range(i,len(input)):
        if input[j] not in output:
            output = output + input[j]
        else:
            if len(output) > len(newString):
                newString = output
            break
    if len(output) > len(newString):
        newString = output

print(newString)


