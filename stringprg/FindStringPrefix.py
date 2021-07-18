st = ["flower", "flow", "flight"]
# Output : fl
prefix = st[0]


def find_prefix(str1, str2):
    local_index = 0
    local_prefix = ''
    while local_index < len(str1) and local_index < len(str2):
        if str1[local_index] == str2[local_index]:
            local_prefix += str1[local_index]
        local_index += 1
    return local_prefix


for index in range(1, len(st)):
    prefix = find_prefix(prefix, st[index])
print(prefix)
