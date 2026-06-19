text = "mississipi"
lst = list(text)
counter = 0

for i in range(len(lst)):
    if lst[i] == 's':
        counter +=1

print(counter)
