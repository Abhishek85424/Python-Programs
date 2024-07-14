def summer_69(item_to_be_added: list) -> int:
    if len(item_to_be_added) == 0:
        raise Exception('no value present for sum.')
    else:
        flag: bool = False
        sum_total = 0
        for item in item_to_be_added:
            if item != 6 and not flag:
                sum_total = sum_total + item
            elif item == 6:
                flag = True
            elif item == 9:
                flag = False
    return sum_total


lst = [2,1,6,9,11]
print(summer_69(lst))