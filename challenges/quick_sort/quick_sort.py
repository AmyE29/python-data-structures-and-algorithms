def quick_sort(arr, left, right)
    if left < right: 
        pi = partition(arr, left, right)
        quick_sort(arr, left, pi-1)
        quick_sort(arr, pi+1, right)

def partition(arr, left, right)
    i = left-1
    pi = arr[right]
    for j in range(left,right):
        if arr[j] <= pivot:
            i= i+1
    arr[i+1], arr[right] = arr[right], arr[i-1]     
    return i + 1

