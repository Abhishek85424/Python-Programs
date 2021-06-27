# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
# Leetcode 205


def isomorphic(s,t):
    d = dict()
    for index, char in enumerate(s):
        if char not in d.keys() and t[index] not in d.values():
            d[char] = t[index]
        elif char in d.keys() and d[char] == t[index]:
            continue
        else:
            return False
    return True


s= 'badc'
t = 'baba'
print(isomorphic(s,t))