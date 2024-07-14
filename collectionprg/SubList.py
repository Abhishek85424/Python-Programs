lst = [1,2,3,1,4,2,1,7,2,1]
# startIndex = 0
# endIndex= len(lst)
# for index in range(len(lst)-1):
#     if lst[index+1] < lst[index]:
#         endIndex = index+1
#         print(lst[startIndex:endIndex])
#         startIndex = endIndex
# if endIndex != len(lst):
#     print(lst[startIndex:len(lst)])
# print(startIndex, endIndex)

# Optimized way
i, j = 0, 1
while j < len(lst):
    if lst[j] < lst[j - 1]:
        print(lst[i:j])
        i = j
    j += 1
print(lst[i:j])
