#5. Longest Palindromic Substring

s = "cbbd"
res = ''
max_len_pal = 0
for i in range(len(s)):
    # Odd Length Palindrom
    l,r= i,i
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r-l+1) > max_len_pal:
            res = s[l:r+1]
            max_len_pal = r-l+1
        l -= 1
        r += 1
    # Even Length
    l, r = i, i+1
    while l >=0 and r < len(s) and s[l] == s[r]:
        if (r-l+1) > max_len_pal:
            res = s[l:r+1]
            max_len_pal = r-l+1
        l -= 1
        r += 1
print(res, max_len_pal)