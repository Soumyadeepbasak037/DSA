arr = "abcdef"

def permutations(arr):
    res = []
    def backtrack(indx,path,arr):
        if(indx == len(arr)):
            res.append(path[:])
            return

        path.append(arr[indx])
        backtrack(indx+1,path,arr)
        path.pop()

        backtrack(indx+1,path,arr)
    backtrack(0,[],arr)
    print(res)

permutations([1,2,3])