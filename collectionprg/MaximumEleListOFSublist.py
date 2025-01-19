nums = [12,-1,-7,8,-15,30,16,28]

start, end, i = 0,len(nums)-1,0
k = 4
max_item = float('-inf')
while start < end:
    max_item = max(max_item, nums[start])
    if i == k:
        print(max_item)
        i = 0
        max_item = float('-inf')
    i += 1
    start += 1

max_item = max(max_item, nums[start])
print(max_item)
