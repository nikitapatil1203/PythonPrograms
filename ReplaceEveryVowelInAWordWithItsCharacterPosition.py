#String input = "apple";         //Output: "1ppl5"

input = "apple"
lst = list(input)
vowels = ['a','e','i','o','u']
output = ""

for i in range(0,len(lst)):
    if lst[i] in vowels:
        output =  output+str(i+1)
    else:
        output = output+lst[i]

print(output)
