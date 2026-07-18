lst = [5, 3, 44, 99, 100, 4, 1, 0]

for j in range (len(lst)-1):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp

print(lst)
