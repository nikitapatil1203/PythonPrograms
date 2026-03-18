# Description: Traverse from top to bottom and print 1, 2, 3, ... but if a duplicate is found, do not increment the value."
# output :
# 1
# 2
# 2
# 3
# 3

list = ["john tom", "john mary", "john tom", "mary anna", "mary anna"]
list2 = []
count = 0

for i in range (0,len(list)):
    if list[i] in list2:
         list2.append(list[i])
         print(count)
    else:
        list2.append(list[i])
        count += 1
        print(count)
