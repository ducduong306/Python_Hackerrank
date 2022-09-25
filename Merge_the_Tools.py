# -*- coding: utf-8 -*-
"""

@author: duong
"""

def merge_the_tools(string, k):
    # your code goes here
    for i in range(int(len(string)/k)):
        ti = string[k*i:k*(i+1)]
        ui = ''
        for s in ti:
            if s not in ui:
                ui += s
        print(ui)
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)