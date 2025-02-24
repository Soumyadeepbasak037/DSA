nums = [2,3,2,1,4]

goal = len(nums)-1

for i in range(len(nums)-1,-1,-1):
    if i+nums[i] >= goal:
        goal = i
        print(goal)
        
