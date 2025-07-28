def combosum(candidates,target):
    result = []
    def backtrack(indx,target,arr):
        if(target == 0):
            result.append(arr[:])
            return
        if (target < 0 or indx == len(candidates)):
            return

        if candidates[indx] <= target:                          
            arr.append(candidates[indx])
            backtrack(indx, target - candidates[indx], arr)
            arr.pop()

        backtrack(indx + 1, target, arr)

    backtrack(0, target, [])
    return result



# candidates = [2, 3, 6, 7]
# target = 7
# print(combosum(candidates, target))

n = 4
k = 2
Output =[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4]
]


inp_arr = [ i for i in range(1,n+1)] 

def combi(inp_arr,k):
    result = []
    def backtrack(indx,arr):
        if(len(arr)==k):
            result.append(arr[:])
            return
        if indx == len(inp_arr):
            return
        
        arr.append(inp_arr[indx])
        backtrack(indx+1,arr)
        arr.pop()

        backtrack(indx+1,arr)

    backtrack(0, [])
    return result

print(combi(inp_arr, k))



#Combinations of phone number   
