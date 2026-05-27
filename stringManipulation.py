#string-concat
name = "Nikita"
surname = "Patil"
full_name = name+" "+surname
print(full_name)

#find length
print(len(full_name))

#lowercase
lowerCaseString = full_name.lower()
print(lowerCaseString)

#replace
text = "my name is nikita"
newText = text.replace("nikita", "nikita patil")
print(newText)

#split
text = "my name is nikita"
newText = text.split(" ")
print(newText)

#Strip
text = "  my name is nikita  "
stripped_text = text.strip()
print(stripped_text)

#subString
str1 = "my name is nikita"
newString = str1[0:9]
print(newString)

#convert to list
str1 = "nikita"
mylist = list(str1)
print(mylist)

