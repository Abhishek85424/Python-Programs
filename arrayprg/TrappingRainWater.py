# 42. Trapping Rain Water leetcode
from typing import List


def trap(height: List[int]) -> int:
    start = 0
    current_element = 1
    trap_water = 0
    current_sum = 0
    valid_trap_start = False
    while start < len(height)-1:
        diff = height[start] - height[current_element]
        if diff > 0:
            current_sum += diff
            valid_trap_start = True
        else:
            start = current_element
        if diff <= 0 and valid_trap_start:
            trap_water += current_sum
            current_sum = 0
            valid_trap_start = False
        current_element += 1
        if current_element == len(height):
            start += 1
            current_element = start+1
            current_sum = 0

    return trap_water

print(trap([4,2,0,3]))