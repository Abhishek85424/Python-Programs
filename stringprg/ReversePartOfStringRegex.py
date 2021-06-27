# i/P :This is Apple
# O/P :Apple is sihT
s = 'This is Apple'
s = s[::-1]
str = s.split()
final_str = []
for index in range(len(str)-1):
    final_str.append(str[index][::-1])
final_str.append(str[len(str)-1])
print(' '.join(final_str))
