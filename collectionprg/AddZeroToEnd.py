lst = [1,0,5,0,0,8,0,9,0]
total_zero = lst.count(0)
new_list = [item for item in lst if item != 0]
new_list.extend([0 for index in range(total_zero)])
print(new_list)