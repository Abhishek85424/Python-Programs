lst = ["rescue","float", "boat", "apple", "elbow", "below", "secure"]
final_lst = []
non_anagram = []
# output : ['rescue', 'secure', 'elbow', 'below', 'float', 'boat', 'apple']
start = 0
end = 1
while start < len(lst)-1:
    if sorted(lst[start]) == sorted(lst[end]):
        final_lst.append(lst[start])
        final_lst.append(lst[end])
    end += 1
    if end == len(lst):
        if lst[start] not in final_lst:
            non_anagram.append(lst[start])
        start += 1
        end = start+1
final_lst.extend(non_anagram)
print(final_lst)
print(non_anagram)