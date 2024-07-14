lst = [[9,3], [20,5], [42, 6, 4.5], [4, 5, 0.58], [78,0], [2,3], [4,6], [0, 0], [0], [16], [None]]
given_number = 0
result = list()
for item in lst:
    if len(item) < 2 or item[len(item)-1] == 0 or None in item:
        continue
    else:
        last_item = item[len(item)-1]
        second_last_item = item[len(item)-2]
        if int(second_last_item/last_item) == given_number:
            result.append(item)

print(result)
