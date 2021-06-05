bracketStr = "[[][[[]]][][[[]]]]"
stack = []
index = 1
for item in bracketStr:
    if item == '[':
        stack.append(index)
        print(index, end='')
        index = index + 1
    else:
        print(stack.pop(), end='')

