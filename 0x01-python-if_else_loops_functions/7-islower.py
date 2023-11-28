#!/usr/bin/python3

def islower(c):
    # Check if the ASCII value of the character is within the range of lowercase letters
    return ord('a') <= ord(c) <= ord('z')

# Example usage:
result = islower('a')
print(result)  # This should print True

result = islower('A')
print(result)  # This should print False
