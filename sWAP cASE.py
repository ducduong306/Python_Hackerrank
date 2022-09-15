# -*- coding: utf-8 -*-
"""

@author: duong
"""

def swap_case(s):
    new_s = ''
    for letter in s: 
        if letter.islower():
            new_s += letter.upper()
        else:
            new_s += letter.lower()
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)