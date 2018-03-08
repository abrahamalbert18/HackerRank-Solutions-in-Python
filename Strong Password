#!/bin/python

import sys

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    count = 0    
    if any(i.isdigit() for i in password) == False:
        count += 1
    if any(i.islower() for i in password) == False:
        count += 1
    if any(i.isupper() for i in password) == False:
        count += 1
    if any(i in special_characters for i in password) == False:
        count+=1
    return max(count,6-n)

if __name__ == "__main__":
    n = int(raw_input().strip())
    password = raw_input().strip()
    answer = minimumNumber(n, password)
    print answer

