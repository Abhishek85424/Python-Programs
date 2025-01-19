"""Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
arr = [1, 2, 3]
ans = list()
final_subset = list()
i = 0


def print_all_subset(arr, ans, i):
    if i == len(arr):
        final_subset.append(ans)
        return
    ans.append(arr[i])
    print_all_subset(arr, ans[:], i + 1)
    ans.pop()
    print_all_subset(arr, ans[:], i + 1)


print_all_subset(arr, ans[:], i)
print(final_subset)

