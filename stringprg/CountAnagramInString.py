st = 'aabacabaa'
s= 'aaba'
k = len(s)
distinct_item = set(s)
current_map = {}
for item in distinct_item:
    current_map[item] = s.count(item)
# print(current_map)
start = 0
end = 0
count = len(current_map)
while end < len(st):
    if st[end] in current_map.keys():
        current_map[st[end]] -= 1
        if current_map[st[end]] == 0:
            count -= 1
    if (end-start)+1 == k:
        if count == 0 :
            print(st[start:end+1])
        if st[end] in current_map.keys():
            current_map[st[end]] += 1
            if current_map[st[end]] > 0:
                count += 1
        start += 1
    end += 1
