import pytest
from merge_sort import merge_sort

def test_unique_values():
    lst = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = merge_sort(lst)
    assert actual == expected

def test_duplicate_value():
    lst = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    actual = merge_sort(lst)
    assert actual == expected

def test_negative_values():
    lst = [20,18,12,8,5,-2]
    expected = [-2,5,8,12,18,20]
    actual = merge_sort(lst)
    assert actual == expected