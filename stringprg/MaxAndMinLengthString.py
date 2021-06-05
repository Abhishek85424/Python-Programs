str = "Hello this is successful stringtest"
str = str.split(' ')
maxStr,minStr = '',''
for index , item in enumerate(str):
    if index ==0 :
        maxStr = item
        minStr = item
    else:
        if len(item) > len(maxStr):
            maxStr = item
        elif len(item) < len(minStr) :
            minStr = item

print(maxStr,minStr)