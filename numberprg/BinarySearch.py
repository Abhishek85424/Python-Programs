# Print in how many passe a given number is found in the array
l = [1,2,3,4,5,6,7,8,9]
start = 0
end = len(l)-1
mid = 0
num = 3
total_pass = 0
found = False
while start <= end:
    mid = int((start+end)/2)
    if l[mid] == num:
        found = True
        break
    elif num > l[mid] :
        start = mid + 1
    else:
        end = mid -1
    total_pass += 1
if found:
    print(f'Number {num} found at position {mid} in total {total_pass} passes.')
else:
    print(f'Number {num} not found in the given list.')
