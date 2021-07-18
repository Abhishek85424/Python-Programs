st = 'a44bd56c3'
start = 0
digits = ''
chars = ''
while start < len(st):
    if st[start].isdigit():
        digits += st[start]
    else:
        if len(digits) != 0 and len(chars) != 0:
            print(chars.strip() * int(digits))
            digits = ''
            chars = ''
        else:
            digits = ''
        chars += st[start]
    start += 1

if len(digits) != 0 and len(chars) != 0:
    print(chars * int(digits))


# digits = re.findall("\\d+", st)
# character = re.findall("[a-z|A-Z]+", st)
# dict = dict(zip(character,digits))
# for key in dict.keys():
#     print(key*int(dict[key]))
