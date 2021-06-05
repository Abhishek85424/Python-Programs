myString = 'India is my country'
for item in set(list(myString)):
    count = myString.count(item)
    if count > 1:
        print(f'Item {item} is duplicated {count} times')