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
# print(subset(nums))

#Combination Sum II


candidates = [2,5,2,1,2]
target = 5
def combinations(candidates,target):
    res = []
    def backtrack(indx,target,arr:list):
        if(target == 0):
            res.append(arr[:])
            return
        if (target < 0 or indx == len(candidates)):
            return
        if(candidates[indx]<=target):
            arr.append(candidates[indx])
            backtrack(indx+1,target-candidates[indx],arr)
            arr.pop()

        backtrack(indx+1,target,arr)
    backtrack(0, target, [])
    return res

print(combinations(candidates,target))