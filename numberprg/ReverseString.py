import math


def reverse_number(x):
    reverse_value = 0
    while x != 0:
        rem = int(math.fmod(x, 10))
        x = int(x / 10)
        # Check if Max range value is greater or last value is also greater than set value to 0
        if (reverse_value > MAX // 10) or (reverse_value == MAX // 10 and
                                           rem > MAX % 10):
            return 0

        if (reverse_value < MIN // 10) or (reverse_value == MIN // 10 and
                                           rem < MIN % 10):
            return 0
        reverse_value = reverse_value * 10 + rem
    return reverse_value


num = 145987
MIN = -2 ** 31
MAX = 2 ** 31 - 1
res = reverse_number(num)
print(res)
