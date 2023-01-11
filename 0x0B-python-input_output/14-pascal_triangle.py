#!/usr/bin/python3
'''
This module defines pascal_triangle function
'''


def pascal_triangle(n):
    '''Creates a list representation of Pascal's Triangle

    Args:
    n (int): size of Pascal's Triangle
    '''
    if n <= 0:
        return []
    pascal = [[] for i in range(n)]
    i = 0
    while i < n:
        if i == 0:
            pascal[0] = [1]

        elif i == 1:
            pascal[1] = [1, 1]

        else:
            pascal[i].append(1)
            for y in range(len(pascal[i - 1]) - 1):
                slide = pascal[i - 1][y:y + 2]
                pascal[i].append(sum(slide))
            pascal[i].append(1)
        i += 1
    return pascal
