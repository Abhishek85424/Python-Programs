lst = [1,2,3,1,4,2,1,7,2,1]
lst = [1,2,3,1,4,2,1,7,2,3]
sublist = []
for i in range(len(lst)):
    sublist.append(lst[i])
    if i < len(lst) -1 and lst[i+1] < lst[i]:
        print(sublist)
        sublist = []
print(sublist)