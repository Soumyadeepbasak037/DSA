n = 3
s = 3

def coin(n,s):
    res = []
    arr = [i for i in range(1,n+1)]
    
    def backtrack(indx,target,path,arr):
        if(target == 0):
            res.append(path[:])
            return
            
        if((indx>=len(arr)) or target<0):
            return
        
        path.append(arr[indx])
        backtrack(indx,target-arr[indx],path,arr)
        path.pop()

        backtrack(indx+1,target,path,arr)

    backtrack(0,s,[],arr)
    print(res)

coin(n,s)
