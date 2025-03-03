nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10

# Naive solution
low = []
high = []
mid = []
for i in range(len(nums)):
    if (nums[i] < pivot):
        low.append(nums[i])
    if (nums[i] > pivot):
        high.append(nums[i])
    if (nums[i] == pivot):
        mid.append(pivot)

joinedlist = low+mid+high
print(joinedlist)

# Something better:

# left,right = 0,len(nums)-1
# i = 0

# while i<=right:
#     if(nums[i]<pivot):
