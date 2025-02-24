# print(original[0:2], original[2:4])
# arr = []
# k = 0


# for i in range(0, m):
#     # print(original[k:n])
#     # print(k, n)
#     temp = (original[k:n])
#     arr.append(temp)
#     k = n
#     n += n

# length = 0
# for i in range(len(arr)):
#     # print(i)
#     length += len(arr[i])


# if (length != len(original)):
#     arr = []
#     print(arr)
# else:
#     # print(length)
#     print(arr)


# k = 0
# arr = []
# for i in range(0, m):
#     # print(original[k:n])  # original[n:2*n]
#     temp = original[k:n]
#     arr.append(temp)
#     k = n
#     n = 2*n
# print(arr)
# ctr = 0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         ctr += 1


original = [1, 1, 1, 1]
m = 4
n = 1
temp = n
k = 0
arr = []

if (m*n != len(original)):
    arr = []
else:
    for i in range(m):
        # print(original[k:n])
        arr += [original[k:n]]
        k = n
        n += temp

print(arr)
