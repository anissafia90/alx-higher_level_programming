#!/usr/bin/python3
def remove_char_at(s, n):
    if 0 <= n < len(s):
        return s[:n] + s[n+1:]
    else:
        return s

# Example usage:
original_string = "example"
position_to_remove = 2
result = remove_char_at(original_string, position_to_remove)

print(result)
