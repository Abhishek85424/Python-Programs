test_str = 'This is string1 with dights'
print(set(list(test_str)))
for char in set(list(test_str)):
    print(f'char  {char} times {test_str.count(char)}')