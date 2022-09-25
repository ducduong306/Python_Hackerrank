# -*- coding: utf-8 -*-
"""

@author: duong
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name_words = s.split(" ")
    capitalized_words = []
    capitalized_string = ''
    for name in name_words:
        if name != '':
            if name[0].islower():
                capitalized_string = capitalized_string + name[0].upper() + name[1:] + ' '
            else:
                capitalized_string = capitalized_string + name + ' '
        else:
            capitalized_string = capitalized_string + ' '
    capitalized_string = capitalized_string.strip()
    
    return capitalized_string

if __name__ == '__main__':
    s = '132 456 Wq  m e'
    print(solve(s) == '132 456 Wq  M E')