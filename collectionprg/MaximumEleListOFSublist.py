nums = [1,-1]

start=0
end = 0
max_elem = float('-inf')
k=1
lst = []
while end < len(nums):
    max_elem = max(max_elem,nums[end])
    if (end-start)+1 == k:
        lst.append(max_elem)
        start +=1
        max_elem = float('-inf')
    end +=1
print(lst)