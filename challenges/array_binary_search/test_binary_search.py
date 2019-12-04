from array_binary_search import binary_search_array

def test_First_Array():
    expected = 2
    actual = binary_search_array([4,8,15,16,23,42], 15)
    assert actual == expected

def test_Second_Array():
    expected = -1
    actual = binary_search_array([4,8,15,16,23,42], 90)
    assert actual == expected
