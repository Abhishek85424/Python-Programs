lst = [2,3,5,2,9,7,1]
start = 0
end =0
k = 3
max_sum = 0
current_sum =0
# while end < len(lst):
#     if end-start == 2:
#         print(lst[start:end+1])
#         current_sum = sum(lst[start:end+1])
#         if max_sum < current_sum:
#             max_sum = current_sum
#         current_sum = 0
#         start = start + 1
#     end = end + 1
# print(max_sum)

while end < len(lst):
    current_sum = current_sum + lst[end]
    if (end - start) + 1 == k:
        print(lst[start:end+1])
        max_sum = max(max_sum, current_sum)
        current_sum = current_sum - lst[start]
        start += 1
        end += 1
    else:
        end +=  1
print(max_sum)
