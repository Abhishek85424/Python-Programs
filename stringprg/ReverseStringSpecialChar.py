my_str ="@bhis$ek"
# special_char = dict()
# rev_str = list()
# for index, item in enumerate(my_str):
#     if not item.isalpha() and not item.isdigit():
#         special_char[index] = item
#     else:
#         rev_str.append(item)
# rev_str = rev_str[::-1]
# for k,v in special_char.items():
#     rev_str.insert(k,v)
# print(''.join(rev_str))

# Optimized way
i, j = 0, len(my_str)-1
my_str = list(my_str)
while i < j:
    if not my_str[i].isalnum():
        i += 1
    elif not my_str[j].isalnum():
        j -= 1
    if my_str[i].isalpha() and my_str[j].isalpha():
        my_str[i], my_str[j] = my_str[j], my_str[i]
        i += 1
        j -= 1
print(''.join(my_str))
