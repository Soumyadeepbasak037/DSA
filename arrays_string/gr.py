# i = str(999)

# sum = 0
# for elem in i:
#     sum += int(elem)
#     # print(sum)
#     if (len(str(sum)) > 1):
#         sum = (sum-int(elem))
#         break
# print(sum)

# n = 6
# arr = [6, 2, 3, 1, 4, 7]
# arr.sort()
# print(arr)
# for i in range(len(arr)-1):
#     if (arr[i+1] != arr[i]+1):
#         print(arr[i]+1)
#         break
#     else:
#         print(n)


string = "jack sparrow"
req_str = string.split(" ")

temp = ""
for i in req_str:
    temp += i.capitalize()
    temp += " "
print(temp)
