s1 = "Hi"
s2 = "This"
s1 = s1+s2
# HiThis
s2 = s1[0:len(s1)-len(s2)]
s1 = s1[len(s2):]
print(s1,s2)