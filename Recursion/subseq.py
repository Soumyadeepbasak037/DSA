text1 = "abcde"
text2 = "ace" 

def subseq(arr):
    result = []
    def backtrack(indx,path):
        if(indx == len(arr)):
            return result.append(path[:])
        
        path.append(arr[indx])
        backtrack(indx+1,path)
        path.pop()

        backtrack(indx+1,path)
        
    backtrack(0,[])
    return result

