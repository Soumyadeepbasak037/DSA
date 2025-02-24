# arr = [-1, 0, 1, 2, -1, -4]
# arr.sort()
# print(arr)
# res = []
# for i, e in enumerate(arr):
#     if (i > 0 and e == arr[i-1]):
#         continue
#     else:
#         for j in range(i+1, len(arr)):
#             # print(e, arr[j])
#             for k in range(i+2, len(arr)):
#                 print(e, arr[j], arr[k])
#                 if (e+arr[j]+arr[k] == 0):
#                     res.append([e, arr[j], arr[k]])

# print(res)

arr = [3, 24, 50, 79, 88, 150, 345]
target = 200

# arr.sort()
l = 0
r = len(arr)-1

while l < r:
    sum = arr[l]+arr[r]

    if (sum < target):
        l += 1
        print(l)
        continue
    if (sum > target):
        r -= 1
        print(r)
        continue
    else:
        print(l+1, r+1, sum)
        break
