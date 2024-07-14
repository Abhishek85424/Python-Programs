s =  'c3[abc]c4[ab]d'
i= 0
digit = ''
str_to_append = ''
final_str = ''
append_str_found = False
while i < len(s):
    if s[i].isalpha() and not append_str_found:
        final_str += s[i]
    elif s[i].isdigit():
        digit += s[i]
    elif s[i] == '[':
        append_str_found = True
    elif append_str_found and s[i] != ']':
        str_to_append += s[i]
    else:
        append_str_found = False
        final_str += str_to_append*int(digit)
        str_to_append = ''
        digit = ''
    i += 1
print(final_str)