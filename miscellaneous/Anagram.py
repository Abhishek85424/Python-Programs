word1 = "listen"
word2 = "silent"

def are_anagrams():
    if len(word1) != len(word2):
        return False
    char_count = dict()
    for char in word1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in word2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    return all(count == 0 for count in char_count.values())
    print(char_count)
if are_anagrams():
    print('Anagaram')
else:
    print('Not')