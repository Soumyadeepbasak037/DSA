addr = "25525511135"

def partition(arr,k):
    res = []
    def backtrack(arr,path,indx):
        if(indx == len(arr) and len(path)==k):
            res.append(path[:])
            return
        if(len(path)>k):
            return
        for i in range(indx+1,len(arr)+1):
            substr = arr[indx:i]
            path.append(substr)
            backtrack(arr,path,i)
            path.pop()
    backtrack(arr,[],0)
    print(res)

partition(addr,3)