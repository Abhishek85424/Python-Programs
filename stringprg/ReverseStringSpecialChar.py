my_str ="@bhis$ek"
special_char = dict()
rev_str = list()
for index, item in enumerate(my_str):
    if not item.isalpha() and not item.isdigit():
        special_char[index] = item
    else:
        rev_str.append(item)
rev_str = rev_str[::-1]
for k,v in special_char.items():
    rev_str.insert(k,v)
print(''.join(rev_str))