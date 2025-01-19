s = "Hello this is successful stringtest"
# s = s.split(' ')
# maxStr, minStr = s[0], s[0]
# for index, item in enumerate(s):
#     if len(item) > len(maxStr):
#         maxStr = item
#     elif len(item) < len(minStr):
#         minStr = item
#
# print(maxStr, minStr)
s = s.split(' ')
max_str = s[0]
min_str = s[0]
for str in s:
    if len(str) > len(max_str):
        max_str = str
    elif len(str) < len(min_str):
        min_str = str
print(max_str, min_str)
