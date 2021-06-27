import re
s = 'Vinay123'
part1 = re.search('[a-zA-Z]+',s)
part2 = re.search('\d+\Z',s)
if part1 and part2:
    part1 = part1.group()
    part2 = part2.group()
    print(part1+part2[::-1])
else:
    print('Either string or number not found in the string')

