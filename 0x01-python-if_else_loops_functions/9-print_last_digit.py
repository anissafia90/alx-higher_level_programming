#!/usr/bin/python3

def print_last_digit(number):
    # Take the absolute value to handle negative numbers
    number = abs(number)

    # Get the last digit using the modulus operator
    last_digit = number % 10

    # Print the last digit
    print(last_digit)

    # Return the value of the last digit
    return last_digit

# Example usage:
result = print_last_digit(12345)
