# coding: utf-8

'''
author: runforever
'''


def bin_search(lst, start, end, value):
    """
    run:
    python -m doctest -v bin_search.py

    doctest:
    >>> bin_search([1], 0, 0, 1)
    0
    >>> bin_search([1], 0, 0, -1)
    -1
    >>> bin_search(range(9), 0, 8, 8)
    8
    >>> bin_search(range(9), 0, 8, 9)
    -1
    >>> bin_search(range(9), 0, 8, 3)
    3
    """
    if start > end:
        return -1

    mid = (start + end) / 2
    search_value = lst[mid]

    if search_value == value:
        return mid
    elif search_value > value:
        end = mid - 1
        return bin_search(lst, start, end, value)
    else:
        start = mid + 1
        return bin_search(lst, start, end, value)
