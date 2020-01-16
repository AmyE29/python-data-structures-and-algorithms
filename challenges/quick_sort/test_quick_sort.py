from quick_sort import quick_sort

def test_unique_values():
    lst = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = quick_sort(lst)
    assert actual == expected

def test_doubles_value():
    lst = [5,12,7,5,5,7,23,16,2,16]
    expected = [2,5,5,5,7,7,12,16,16,23]
    actual = quick_sort(lst)
    assert actual == expected

def test_negative_values():
    lst = [8,4,23,-42,16,-15]
    expected = [-42,-15,4,8,16,23]
    actual = quick_sort(lst)
    assert actual == expected

def test_reverse_values():
    lst = [[20,18,12,8,5,-2]]
    expected = [-2,5,8,12,18,20]
    actual = quick_sort(lst)
    assert actual == expected
