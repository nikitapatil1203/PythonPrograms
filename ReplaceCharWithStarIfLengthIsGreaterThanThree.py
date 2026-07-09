# input = "Same ytegde eat"
# o/p =  "**** ****** eat "

text = "Same ytegde eat"
lst = text.split()
outputString = ""


for element in lst:
    if len(element) > 3:
        list1 = list(element)
        print(list1)
        for i in list1:
            outputString = outputString+"*"
        outputString = outputString+" "
    else:
        outputString = outputString + element + " "


print(outputString)
