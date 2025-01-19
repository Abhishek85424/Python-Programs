lst = [3, -1, -3, 1, 2, -2, 4]
start = 0
seen = set()
for num in lst:
    if -num in seen:
        print((num,-num))
    seen.add(num)