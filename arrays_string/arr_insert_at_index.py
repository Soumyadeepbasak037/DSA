arr = [0,1,2,3,4]
def insert_at_arr(arr,index,new_elem):
    arr.append(arr[-1])
    i = len(arr)-3
    while(i>index-1):
        arr[i+1] = arr[i]
        i=i-1
    arr[i+1] = new_elem
    print(arr)
    
insert_at_arr(arr,2,8)