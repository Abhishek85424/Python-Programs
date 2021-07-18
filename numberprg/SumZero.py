lst = [-3, -2, -1, 2]
start = 0
final_list = []
end = len(lst)-1
while start < end:
    if lst[start] >= 0:
        break
    if lst[start]+lst[end] == 0:
        final_list.append(lst[start])
        final_list.append(lst[end])
        break
    if abs(lst[start]) > lst[end]:
        start += 1
    else:
        end -= 1

if len(final_list) == 0:
    print('undefined')
else:
    print(final_list)
