def insert_shift_array(array, value):
    nums = (len(array) + 1) // 2
    new_array = []
    for i in range(nums):
        new_array.append(array[i])
    new_array.append(value)
    for i in range(nums, len(array)):
        new_array.append(array[i])
    return(new_array)
