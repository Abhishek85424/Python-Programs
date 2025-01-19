print([0]*5)
"""
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""
s1 = "ab"
s2 = "eidabooo"

orignalFrequency = [0]*26
temp_frequency = [0]*26
for char in s1:
    orignalFrequency[ord(char)-ord('a')] += 1
start,end = 0,0
exist = False
while end < len(s2):
    temp_frequency[ord(s2[end]) - ord('a')] += 1
    if end-start+1 == len(s1):
        if orignalFrequency == temp_frequency:
            exist =True
            break
        temp_frequency[ord(s2[start]) - ord('a')] -= 1
        start += 1
    end += 1

if exist:
    print('Exist')
else:

    print('No')
print(orignalFrequency)