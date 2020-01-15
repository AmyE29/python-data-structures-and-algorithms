import pytest
from insert_sort import insertion_sort


def test_insertion_sort():
    lst = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = insertion_sort(lst)
    assert actual == expected

def test_reverse_sorted():
    lst = [20,18,12,8,5,-2]
    expected = [-2,5,8,12,18,20]
    actual = insertion_sort(lst)
    assert actual == expected

def test_duplicate_values():
    lst = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    actual = insertion_sort(lst)
    assert actual == expected

def test_nearly_sorted():
    lst = [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]
    actual = insertion_sort(lst)
    assert actual == expected

   

