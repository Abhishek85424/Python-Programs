# Move all the zero at the end
lst = [1,0,5,0,0,8,0,9,0]
total_zero = lst.count(0)
new_list = [item for item in lst if item != 0]
new_list.extend([0 for index in range(total_zero)])
print(new_list)

# Optimized Approach
l = [1,2,0,4,-1,5,6,0,0,7,0]
j = 0
for i in range(len(l)):
    if l[i] != 0:
        l[i], l[j] = l[j], l[i]
        j += 1
print(l)