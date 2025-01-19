# Rotate a list by K position
nums = [1, 2, 3, 4, 5, 6, 7]
# nums = [1, 2, 3, 4]
k = 11
total_items = len(nums) - 1
k = k % len(nums)


def rotate_array(l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
l, r = 0, total_items
rotate_array(l,r)

l, r = 0, k-1
rotate_array(l,r)
l, r = k, total_items
rotate_array(l,r)

print(nums)