def permute_unique(inp_arr):
    arr = sorted(inp_arr)
    # print(arr)
    res = []
    aux = [False for i in range(len(arr))]
    
    def backtrack(arr,aux,path):
        if(len(path) == len(arr)):
            return res.append(path[:])
            
        for i in range(len(arr)):
            if aux[i]:
                continue

        
            if i > 0 and arr[i] == arr[i - 1] and not aux[i - 1]:
                continue

            aux[i] = True
            path.append(arr[i])
            backtrack(arr,aux,path)
            path.pop()
            aux[i] = False
                    
    backtrack(arr,aux,[])
    print(res)
    
permute_unique([1,1,2])