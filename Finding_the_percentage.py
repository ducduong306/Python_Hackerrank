# -*- coding: utf-8 -*-
"""

@author: duong
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    student_average_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        student_average_marks[name] = sum(scores)/len(scores)
    query_name = input()
    print("{:0.2f}".format(student_average_marks[query_name]))
    