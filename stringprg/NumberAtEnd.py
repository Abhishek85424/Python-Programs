s = 'ass2b4ccd3p5s5sf'
# s = list(s)
# # oo/p = abccdp24355

l = 0
r = len(s)-1
s = list(s)
# while l < r:
#     if s[l].isdigit() and s[r].isalpha():
#         s[l], s[r] = s[r], s[l]
#         l += 1
#         r -= 1
#     elif s[l].isalpha():
#         l +=1
#     else:
#         print(s[r])
#         r -= 1
# print(''.join(s))

while l<r:
    if s[l].isalpha():
        l += 1
    elif s[l].isdigit() and s[r].isalpha():
        s[l], s[r] = s[r], s[l]
        l, r = l+1, r-1
    else:
        r -=1
print(''.join(s))