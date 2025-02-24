import math
arr = [7,1,5,3,6,4]

# for i in arr:
#     for j in range(i+1,len(arr)):
#         print(i,arr[j])

# max = 0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         # print(arr[i]-arr[j])
#         if(arr[j]-arr[i] > max):
#             max = arr[j]-arr[i]
#             # print(arr[i],arr[j],max)
# # print(max)      
        
ptr1 = 0
ptr2 = 1
max2 = 0

while ptr2<len(arr):
    if(arr[ptr1]<arr[ptr2]):
        profit = arr[ptr2]-arr[ptr1]
        max2= max(max2,profit)
    else:
        ptr1+=1
    ptr2+=1
    
    
print(max2)