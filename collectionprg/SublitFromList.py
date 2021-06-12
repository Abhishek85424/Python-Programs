lst = [1,2,3,1,4,2,1,7,2,3]
start = 0
current = 1
prev = 0
final_list = []
while current < len(lst):
    if lst[current] < lst[prev]:
        final_list.append(lst[start:current])
        start = current
    current += 1
    prev += 1
if start != len(lst):
    final_list.append(lst[start:len(lst)])
print(final_list)