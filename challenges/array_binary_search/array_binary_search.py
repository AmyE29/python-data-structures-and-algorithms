def binary_search_array(lst, val):
        left_index = 0
        right_index = (len(lst)-1)
        while left_index <= right_index:
            middle = left_index + (right_index - left_index)/2

            if val == lst[middle]:
                return middle

            elif val < lst[middle]:
                right_index = (middle -1)

            elif val > lst[middle]:
                left_index = (middle +1)

        return -1
