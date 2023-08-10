#!/usr/bin/python3
import random

def analyze_last_digit(number):
    digit = abs(number) % 10
    if number < 0:
        digit = -digit
    
    result = ""
    if digit > 5:
        result = "greater than 5"
    elif digit == 0:
        result = "0"
    else:
        result = "less than 6 and not 0"
    
    return digit, result

number = random.randint(-10000, 10000)
last_digit, result_text = analyze_last_digit(number)

print("Last digit of {} is {} and is {}".format(number, last_digit, result_text))
