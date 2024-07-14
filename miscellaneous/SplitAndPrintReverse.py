s1="Hi This is my first program"
# output = ma rgor pt sr ifyms isihTiH
s1 = list(s1)
ptr1, ptr2 = 0, len(s1)-1

while ptr1<=ptr2:
    if s1[ptr1] == ' ':
        ptr1 += 1
    elif s1[ptr2] == ' ':
        ptr2 -= 1
    else:
        s1[ptr1], s1[ptr2] = s1[ptr2], s1[ptr1]
        ptr1 += 1
        ptr2 -= 1

print(''.join(s1))