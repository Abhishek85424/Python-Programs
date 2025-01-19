def longest_common_prefix(strs):
    if not strs:
        return ""

    # Start with the first string as the prefix
    prefix = strs[0]

    # Compare the prefix with each string in the list
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            # Shorten the prefix until it matches
            prefix = prefix[:-1]
            # If the prefix becomes empty, there's no common prefix
            if not prefix:
                return ""

    return prefix

# Example usage
words = ["flower", "flow", "flight",'xyxz']
result = longest_common_prefix(words)
print("Longest Common Prefix:", result)
