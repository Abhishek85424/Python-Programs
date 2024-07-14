def consecutive_one(lst_values: list) -> int:
    max_ones = 0
    current_count =0
    for number in lst_values:
        if number:
            current_count = current_count + 1
        else:
            max_ones = max(max_ones,current_count)
            current_count = 0
    max_ones = max(max_ones, current_count)
    return max_ones


print(consecutive_one([1,0,1,1,0,1]))


