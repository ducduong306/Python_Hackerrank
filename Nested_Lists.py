# -*- coding: utf-8 -*-
"""

@author: duong
"""


if __name__ == '__main__':
    nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name,score])
        
    sorted_nested_list = sorted(nested_list, key = lambda x:x[1],reverse=True)
    second_highest = sorted(set([score for name, score in sorted_nested_list]))[1]
    output_names = []

    output_names = [name for name, score in sorted_nested_list if score ==second_highest]
    output_names = sorted(output_names, reverse=False)
    for name in output_names:
        print(name)