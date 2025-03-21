arr = [1, 2, 3, 4, 5, 8, 9]

target = 2

low = 0
high = len(arr)-1


while low <= high:
    mid = (low+high)//2
    if (arr[mid] == target):
        print(mid)
        break
    if (target > arr[mid]):
        low = mid+1
    if (target < arr[mid]):
        high = mid-1


def binary_search(arr, target, high, low):
    if low >= high:
        return
    mid = (low+high)//2
    if (arr[mid] == target):
        return mid
    if (target < arr[mid]):
        return binary_search(arr, target, mid-1, low)
    if (target > arr[mid]):
        return binary_search(arr, target, high, mid+1)


print(binary_search(arr, target, len(arr)-1, 0))
