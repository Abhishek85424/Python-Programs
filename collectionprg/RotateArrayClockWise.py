# Rotate a list by K position
nums = [1, 2, 3, 4, 5, 6, 7]
nums = [1, 2, 3, 4]
k = 2
def reverse(nums,start,end):
    while start < end:
        temp = nums[end]
        nums[end] = nums[start]
        nums[start] = temp
        start += 1
        end -= 1


end = len(nums) - 1
reverse(nums, 0, end)
reverse(nums, 0, k-1)
reverse(nums, k, end)
print(nums)

