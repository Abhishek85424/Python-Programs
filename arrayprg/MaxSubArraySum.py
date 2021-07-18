def max_sub_array_sum(arr,k):
    start = 0
    current_element_ptr = 0
    max_sum = 0
    current_total = 0
    while current_element_ptr < len(arr):
        current_total += arr[current_element_ptr]
        if (current_element_ptr-start)+1 == k:
            max_sum = max(max_sum, current_total)
            current_total -= arr[start]
            start += 1
        current_element_ptr += 1
    return max_sum


arr = [4, 2, 1, 6, 2]
k = 4
result = max_sub_array_sum(arr, k)
print(result)
