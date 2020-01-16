from quick_sort import quick_sort, partition

def test_unique_values():
    arr = [8,4,23,42,16,15]
    quick_sort(arr, 0, len(arr) -1)
    assert arr == [4,8,15,16,23,42]

def test_doubles_value():
    arr = [5,12,7,5,5,7,23,16,2,16]
    quick_sort(arr, 0, len(arr) -1)
    assert arr == [2,5,5,5,7,7,12,16,16,23]

def test_negative_values():
    arr = [8,4,23,-42,16,-15]
    quick_sort(arr, 0, len(arr) -1)
    assert arr == [-42,-15,4,8,16,23]

def test_reverse_values():
    arr= [20,18,12,8,5,-2]
    quick_sort(arr, 0, len(arr) -1)
    assert arr == [-2,5,8,12,18,20]

def test_part_partition():
    arr= [0,5,2,6,8,4]
    actual = partition (arr, 0, len(arr)-1)
    assert arr == [0,2,4,6,8,5]

def test_quicksort():
    arr= [0,5,2,6,8,4]
    quick_sort(arr, 0, len(arr) -1)
    assert arr == [0,2,4,5,6,8,]
