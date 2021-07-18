st = 'apple456shwetha2123903'
final_str = ''
start = 0
digit_count = 0
while start < len(st):
    if st[start].isdigit():
        digit_count += 1
    else:
        if digit_count:
            final_str += st[start-digit_count:start][::-1]
            digit_count = 0
        final_str += st[start]
    start += 1
if digit_count:
    final_str += st[start-digit_count:start][::-1]
print(final_str)