
input = "NikitaPatil"
# output: AtIkIn
newString = input[0].upper()
rev =""

for i in range(1, len(input)):
    if input[i].isupper():
        break
    else:
        newString = newString + input[i].upper()

j=len(newString)-1
while j>=0:
    if j%2==0:
        rev = rev + newString[j].lower()
    else:
        rev = rev + newString[j]
    j -= 1

print(rev)
