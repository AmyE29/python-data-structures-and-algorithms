def quick_sort(arr, left, right):
    if right - left <= 0:
        return 
    pi = partition(arr, left, right)
    quick_sort(arr, left, pi-1)
    quick_sort(arr, pi+1, right)

def partition(arr, left, right):
    pivot =  arr[right]
    low = left - 1
    for i in range(left,right):
        if arr[i] <= pivot:
            low +=1
            swap(arr, i, low)
 
    swap(arr, right, low + 1)
    
    return low + 1

def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]
