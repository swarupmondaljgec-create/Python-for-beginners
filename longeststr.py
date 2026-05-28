def longest_string_length(strings):
    return max((len(s) for s in strings), default=0)
words = ["apple", "banana", "cherry"]
print(longest_string_length(words))  # Output: 6
