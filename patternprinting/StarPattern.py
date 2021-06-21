# print pattern like
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

n = 5
i = 1
while i < (n*2):
    if i <= n:
        print('*'*i)
    else:
        print('*'*(n*2-i))
    i += 1
