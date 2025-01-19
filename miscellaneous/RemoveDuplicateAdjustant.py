def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the duplicate
        else:
            stack.append(char)
    return ''.join(stack)

# Example usage
input_str = "acaaabbbacdddd"
result = remove_adjacent_duplicates(input_str)
print("Result:", result)  # Output: "ca"
