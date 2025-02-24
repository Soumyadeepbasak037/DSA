# s

# if (curr_sum >= curr_max):
#     curr_max = curr_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
req_subarr = []

length = len(arr)
curr_max = min(arr)
curr_sum = 0
for i in range(len(arr)):
    temp_arr = []
    curr_sum = 0
    for j in range(i, len(arr)):
        temp_arr.append(arr[j])
        print(temp_arr)
        curr_sum += temp_arr[-1]
        if (curr_sum >= curr_max):
            req_subarr = temp_arr
            curr_max = curr_sum

print(curr_max, req_subarr)
