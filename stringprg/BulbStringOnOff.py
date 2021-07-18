st = 'oxox'
k = 20
start = 1
while start <=k:
    if st[0] == 'x':
        st = 'o'+st[1:]
    else:
        st = 'x' + st[1:]
        index = 1
        while index<len(st):
            if st[index] == 'o':
                st = st[0:index]+'x'+st[index+1:]
            else:
                st = st[0:index] + 'o' + st[index + 1:]
                break
            index +=1
    start += 1
    print(st)
# print(st)