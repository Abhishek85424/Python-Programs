dict1 = {'a':100,'b':200,'c':300}
dict2 = {'a':300,'b':200,'d':400,'e':123}
all_keys = set(dict1.keys())
all_keys = all_keys.union(set(dict2))
for key in all_keys:
    if key in dict1.keys() and key in dict2.keys():
        dict1[key] = [dict1[key],dict2[key]]
    elif key in dict2.keys():
        dict1[key] = dict2[key]
print(dict1)