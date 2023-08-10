#!/usr/bin/python3
# 8-uppercase.py

def uppercase(input_str):
    """Print a string in uppercase."""
    for c in input_str:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - 32)
        print(f"{c}", end="")
    print("")

# Test the function
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    uppercase(input_string)
