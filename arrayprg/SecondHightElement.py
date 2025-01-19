lst = [2, 3, 3, 3, 3, 3, 3, 3, 1, -144, 6, 8, -2, 5, 3, -22, 66, -1, 0]
lst = [1,5,4,6,3,2]
lst = [78,6,48,90,89,88,90]
highest = float('-inf')
second_highest = float('-inf')
for num in lst:
    if num > highest:
        highest, second_highest = num, highest
    elif num > second_highest and num != highest:
        second_highest = num
print(second_highest)
