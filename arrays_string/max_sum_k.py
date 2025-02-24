nums = [1, 5, 4, 2, 9, 9, 9]
k = 3

# for i in range(len(nums)):
#     for j in range(i, i+3):
#         print(nums[i], ":", nums[j])

# max_ = 0
# for i in range(len(nums)):
#     max_arr = []
#     temp_max = 0
#     if (temp_max >= max_):
#         max_ = temp_max
#     for j in nums[i:i+k]:
#         temp_max += j

nums = [1, 5, 4, 2, 9, 9, 9]
k = 3

# for i in range(len(nums)):
#     for j in range(i, i+3):
#         print(nums[i], ":", nums[j])

# max_ = 0
# for i in range(len(nums)):
#     max_arr = []
#     temp_max = 0
#     if (temp_max >= max_):
#         max_ = temp_max
#     for j in nums[i:i+k]:
#         temp_max += j

#     print(nums[i:i+k])

max_num = 0
temp_max = 0
for i in range(len(nums)):
    arr = []
    if (temp_max >= max_num):
        max_num = temp_max
    print(max_num)
    temp_max = 0
    for j in nums[i:i+k]:
        arr.append(j)
        temp_max += j
        print("temp max: ", temp_max)

print(max_num)
