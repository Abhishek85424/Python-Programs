lst = [1,0,2,3,0,4,5,0]
current_ptr = 0
while current_ptr < len(lst):
    if lst[current_ptr] == 0:
        last_ptr = len(lst)-1
        while last_ptr > current_ptr:
            lst[last_ptr] = lst[last_ptr - 1]
            last_ptr = last_ptr - 1
        current_ptr = current_ptr + 2
    else:
        current_ptr = current_ptr + 1
print(lst)
