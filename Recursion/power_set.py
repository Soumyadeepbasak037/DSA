nums = [1,2,3]

def subset(nums):
    res = []
    def backtrack(indx,arr):
        if(indx == len(nums)):
            res.append(arr[:])
            return
        
        #take
        arr.append(nums[indx])
        backtrack(indx+1,arr)
        arr.pop()
        #not take
        backtrack(indx+1,arr)
    backtrack(0, [])
    return res
print(subset(nums))