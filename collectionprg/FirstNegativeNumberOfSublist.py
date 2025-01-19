lst = [12,-1,-7,8,-15,30,16,28]
start = 0
end = len(lst) -1
k = 3
i = 0
# Optimized Method
negative_num = 0
while start < end:
    if negative_num == 0 and lst[start] < 0:
        negative_num = lst[start]
    if i == k-1 and negative_num != 0:
        print(negative_num)
        negative_num = 0
        i = 0
    i += 1
    start += 1

