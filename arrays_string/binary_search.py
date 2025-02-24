

arr = list(range(1, 1_000_001))

def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    
    
    while low<=high:
        mid = (low+high)//2
        # print(arr[low:high])
        
        if(arr[mid]==target):
            return mid
        
        elif(arr[mid]>target):
            high = mid-1
            
        else:
            low = mid+1
        
    return -1

print(binary_search(arr,990))
        