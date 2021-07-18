str = 'peaches, grapes, apples, apples, grapes, watermelon, apples, peaches'
str = str.split(',')
item_dict = dict()
for key in str:
    key = key.strip()
    if key in item_dict.keys():
        item_dict[key] += 1
    else:
        item_dict[key] = 1

item_dict = dict(sorted(item_dict.items()))
print(item_dict)

