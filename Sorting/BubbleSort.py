#  Bubble sort
l = [4, 3, 7, 1, 5]
for index in range(len(l)):
    swapped = False
    for j_index in range(1, len(l)-index):
        if l[j_index-1] > l[j_index]:
            l[j_index], l[j_index-1] = l[j_index-1], l[j_index]
            swapped = True
    if not swapped:
        break
print(l)
