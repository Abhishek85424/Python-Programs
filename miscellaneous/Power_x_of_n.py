x = 2.00000
binaryForm = 10
ans = 1
while binaryForm != 0:
    if binaryForm % 2 == 1:
        ans = ans *x
    x *=x
    binaryForm /= 2
print(ans)