#!/usr/bin/python3

def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            # Keep non-lowercase characters unchanged
            uppercase_char = char

        print(uppercase_char, end="")

    # Print a newline character at the end
    print()

# Example usage:
uppercase("Hello, World!")
