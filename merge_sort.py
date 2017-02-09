# coding: utf-8

'''
author: runforever
'''

def merge(left_lst, right_lst):
    """
    >>> merge([1], [1])
    [1, 1]
    >>> merge([1], [2])
    [1, 2]
    >>> merge([3, 4], [1, 2])
    [1, 2, 3, 4]
    >>> merge([1, 3], [2, 4, 5])
    [1, 2, 3, 4, 5]
    """
    sorted_list = []

    while len(left_lst) > 0 and len(right_lst) > 0:
        left_value, right_value = left_lst[0], right_lst[0]
        if left_value <= right_value:
            sorted_list.append(left_value)
            left_lst = left_lst[1:]
        else:
            sorted_list.append(right_value)
            right_lst = right_lst[1:]

    sorted_list.extend(left_lst)
    sorted_list.extend(right_lst)
    return sorted_list


def merge_sort(lst):
    """
    run:
    python -m doctest -v bin_search.py

    doctest:
    >>> merge_sort([1])
    [1]
    >>> merge_sort([2, 1])
    [1, 2]
    >>> merge_sort([3, 4, 1, 2, 6, 9, 8, 5, 7])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(lst) <= 1:
        return lst

    start, end = 0, len(lst)
    mid = (start + end) / 2

    left_lst = merge_sort(lst[:mid])
    right_lst = merge_sort(lst[mid:])
    return merge(left_lst, right_lst)
