st= 'aaaabbaa'
lst = []
for index in range(len(st)):
    cols = []
    for j_index in range(len(st)):
        if j_index >= index:
            if index == j_index:
                cols.append(j_index)
                cols[j_index] = 1
            else:
                if st[index] == st[j_index]:
                    cols.append(j_index)
                    cols[j_index] = 1
                else:
                    cols.append(j_index)
                    cols[j_index] = 0
        else:
            cols.append(j_index)
            cols[j_index] = 0
    lst.append(cols)
    print(cols)

    for index in range(len(st)):
        for j_index in range(len(st)):
            if lst[index][index] == lst[index][j_index] and lst[index-1] == lst[j_index-1]:
                lst[index][j_index] =1

# print(lst)