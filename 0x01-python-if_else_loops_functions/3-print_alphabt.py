#!/usr/bin/python3
output = [chr(letter) for letter in range(97, 123) if chr(letter) != 'q' and chr(letter) != 'e']
print("".join(output), end="")
