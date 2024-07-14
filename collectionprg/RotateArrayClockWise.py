# Rotate a list by K position
nums = [1, 2, 3, 4, 5, 6, 7]
nums = [1, 2, 3, 4]
k = 3
temp = list()
for index,value in enumerate(nums):
    list.insert((index+k) % len(nums),value)

print(temp)
