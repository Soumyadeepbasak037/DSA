arr = [2, 3, 5, 1, 9]
req_sum = 5


# for i in range(len(arr)):
#     temp_arr.append(arr[i])
#     for j in range(i, len(arr)):
#         temp = (arr[i]+arr[j])
#         temp_arr.append(arr[j])
#         if temp > sum:
#             # print(temp)
#             temp_arr = []
#             break
#         elif temp == sum:
#             print(temp)
#             print(temp_arr)
#             continue

arr.sort()
# print(arr)
temp_arr = []
sum = 0
tmp = 0

for i in range(len(arr)):
    sum = arr[i]
    for j in range(i, len(arr)):
        sum += arr[j]
        print(sum)
        if (sum == req_sum):
            print(sum)
        else:
            break
