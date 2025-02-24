
import math
def search(arr, n, offset=0):
    start = 0
    end = len(arr)
    
    if end == 0:
        print("Not found")
        return
    
    mid = math.floor((start + end) / 2)
    
    if n == arr[mid]:
        print(mid + offset)
    
    elif n < arr[mid]:
        search(arr[0:mid], n, offset)
        print(arr[0:mid])
    else:
        search(arr[mid:end], n, offset + mid)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# search(arr,6)



array = {3, 4, 6, 7, 9, 12, 16, 17}

def binary_search(arr,target):
    start = 0
    end = len(arr)
    mid = math.floor(start+end //2)
    
    
    