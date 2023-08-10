#!/usr/bin/python3
# 7-islower.py

def islower(c):
    """Check if a character is lowercase."""
    return 'a' <= c <= 'z'

# Test cases
print(islower('a'))  # True
print(islower('Z'))  # False
print(islower('5'))  # False
print(islower('b'))  # True
