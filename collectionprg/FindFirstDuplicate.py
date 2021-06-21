lst = [10, 5, 3, 4, 3, 5, 6]
no_dups = set()
first_dup = -1
# Optimized way
for item in lst:
    if item in no_dups:
        first_dup = item
        break
    else:
        no_dups.add(item)
print(first_dup)

# Brute Force
start = 0
end = 1
min_index = -1
while start < len(lst) and end < len(lst):
    if lst[start] == lst[end]:
        if min_index == -1:
            min_index = end
        else:
            min_index = min(min_index, end)
        start += 1
        end = start + 1
    end += 1
    if end == len(lst):
        start += 1
        end = start + 1


print(lst[min_index])
