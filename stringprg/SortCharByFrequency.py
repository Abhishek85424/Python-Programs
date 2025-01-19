# Leetcode #451
s = 'acBaBABaca'
# op aaaaBBBccA
frequency_count = dict()
for item in s:
    if item in frequency_count:
        frequency_count[item] += 1
    else:
        frequency_count[item] = 1
frequency_count = dict(sorted(frequency_count.items(),
                              key=lambda item: item[1],reverse=True))
s = ''
for k, v in frequency_count.items():
    s += k*v
print(s)
