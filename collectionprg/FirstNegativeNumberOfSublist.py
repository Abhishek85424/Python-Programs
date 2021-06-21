lst = [12,-1,-7,8,-15,30,16,28]
start = 0
first_negative_number = 0
end = 0
k = 3
negative_list= []
# Optimized Method
while end < len(lst):
    if lst[end] < 0:
        negative_list.append(lst[end])
    if (end-start)+1 == k:
        if len(negative_list) == 0:
            print(0)
        else:
            print(negative_list[0])
            if lst[start] == negative_list[0]:
                negative_list.pop(0)
        start += 1
    end += 1

#  Brute Force Method
while end < len(lst):
    if lst[end] < 0 and first_negative_number ==0:
        first_negative_number = lst[end]
    if (end-start)+1 ==k:
        print(first_negative_number)
        end = start
        start += 1
        first_negative_number = 0

    end = end+1

