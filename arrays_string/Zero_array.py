from operator import truediv
#
# nums = [4,3,2,1]
# queries = [[1,3],[0,2]]

nums = [1, 0, 1]
queries = [[0, 2]]

for query in queries:
    r1 = query[0]
    r2 = query[1]

    for i in range(r1,r2+1):
        if(nums[i]!=0):
            nums[i] = nums[i]-1

print(nums)
if 0 not in nums:
    print("false")

# for i in nums:
#     if i == 0:
#         flag = True
#     else:
#         flag = False
#         break
