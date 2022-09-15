# -*- coding: utf-8 -*-
"""

@author: duong
"""



if __name__ == '__main__':
    N, M = map(int, input().split())
    
    symbol = '.|.'
    mid = int((N-1)/2)
    for i in range(mid):
        print(((1+2*i)*symbol).center(M,'-'))
    print('WELCOME'.center(M,'-'))
    for i in range(mid-1,-1,-1):
        print(((1+2*i)*symbol).center(M,'-'))
    
    
    