test_str = 'This is string1 with dights'
print(set(list(test_str)))
for char in set(list(test_str)):
    print(f'char  {char} times {test_str.count(char)}')

# Optimized approach
char_count = dict()
for char in test_str:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)