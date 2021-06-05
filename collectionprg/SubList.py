list = [1,2,5,3,4,2,1]
startIndex = 0
endIndex= len(list)
for index in range(len(list)-1):
    if list[index+1] < list[index]:
        endIndex = index+1
        print(list[startIndex:endIndex])
        startIndex = endIndex
if endIndex != len(list):
        print(list[startIndex:len(list)])
print(startIndex,endIndex)
