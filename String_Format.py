# -*- coding: utf-8 -*-
"""

@author: duong
"""

def print_formatted(number):
    # your code goes here
    spaces = len("{0:b}".format(number))
    # for i in range(1,number+1):       
    #     print("{0:d}".format(i).rjust(spaces+1,' ') + "{0:o}".format(i).rjust(spaces+1,' ') + "{0:X}".format(i).rjust(spaces+1, ' ') + "{0:b}".format(i).rjust(spaces+1, ' '))
    for i in range(1, number+1):
        print("{0:{space}d} {0:{space}o} {0:{space}X} {0:{space}b}".format(i, space=spaces))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
    