def get_subset(nums, ans, i, final_set):
    if i == len(nums):
        final_set.append(ans)
        return
    ans.append(nums[i])
    get_subset(nums, ans[:], i + 1, final_set)
    ans.pop()
    idx = i + 1
    while idx < len(nums) and nums[idx-1] == nums[idx]:
        idx += 1
    get_subset(nums, ans[:], idx, final_set)

final_set = list()
ans = list()
i = 0
nums = [4,4,4,1,4]
nums.sort()
get_subset(nums, ans[:],i, final_set)
print(final_set)