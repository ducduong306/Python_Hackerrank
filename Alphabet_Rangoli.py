# -*- coding: utf-8 -*-
"""

@author: duong
"""

def print_rangoli(size):
    # your code goes here
    list_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    line_length = size*2-1 + size*2-1-1
    for i in range(size):
        list_letter = list_alphabets[size-1:size-i-1:-1] + list_alphabets[size-i-1] + list_alphabets[size-i:size]
        print(('-'.join(list_letter)).center(line_length,'-'))
        
    for i in range(size-2,-1,-1):
        list_letter = list_alphabets[size-1:size-i-1:-1] + list_alphabets[size-i-1] + list_alphabets[size-i:size]
        print(('-'.join(list_letter)).center(line_length,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)