arr = [-2,-3,4,-1,-2,1,5,-3]

#O(n^2) 
# for i in range(len(arr)):
#     sum = 0
#     for j in range(i,len(arr)):
#         sum+=arr[j] #for this 
#         print(sum,arr[i:j])

#Kadane's Algorithm

max = 0
sum = 0
for i in range(len(arr)):
    sum += arr[i]
    
    if(sum>max):
        max = sum
    if(sum<0):
        sum = 0
print(max)