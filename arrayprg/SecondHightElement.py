lst = [2, 3, 3, 3, 3, 3, 3, 3, 1, -144, 6, 8, -2, 5, 3, -22, 66, -1, 0]
if len(lst) == 0:
    print('Given list is empty !!')
    exit(1)
start = 0
min_var1 = lst[0]
min_var2 = lst[0]
while start < len(lst):
    if lst[start] < min_var1:
        min_var1 = lst[start]
    elif lst[start] < min_var2:
        min_var2 = lst[start]
    start += 1
print(min_var2)
