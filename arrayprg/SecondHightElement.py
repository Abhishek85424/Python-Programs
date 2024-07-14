lst = [2, 3, 3, 3, 3, 3, 3, 3, 1, -144, 6, 8, -2, 5, 3, -22, 66, -1, 0]
# lst = [1,5,4,6,3,2]
if len(lst) == 0:
    print('Given list is empty !!')
    exit(1)
elif len(lst)<2:
    raise Exception('Less then 2 items in lists')

start = 0
min_var1, min_var2 = max(lst[0],lst[1]), min(lst[0],lst[1])
for item in lst[2:]:
    if item > min_var1:
        min_var2 = min_var1
        min_var1 = item



print(min_var2)
