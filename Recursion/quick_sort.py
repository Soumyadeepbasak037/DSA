arr = [1, 6, 9, 7, 0, 2, 3, 8]


def quick_sort(arr, pivot):
    temp = arr[:pivot]
    temp2 = arr[pivot:len(arr)]
    quick_sort(temp, len(temp)//2)
    quick_sort(temp2, len(temp2)//2)
