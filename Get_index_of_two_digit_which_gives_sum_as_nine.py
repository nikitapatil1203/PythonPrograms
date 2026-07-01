lst = [1,2,5,6,4,7]
total = 0
pairs = []


for i in range(len(lst)):
    for j in range (i,len(lst)):
        total = lst[i]+lst[j]
        if total == 9:
            pairs.append((i,j))

print(pairs)


