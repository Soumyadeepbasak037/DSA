# arr = [0, 1, 2, 3, 4]


# def insert_at_arr(arr, index, new_elem):
#     arr.append(arr[-1])
#     i = len(arr)-3
#     while (i > index-1):
#         arr[i+1] = arr[i]
#         i = i-1
#     arr[i+1] = new_elem
#     print(arr)


# insert_at_arr(arr, 2, 8)


# print(str_int)
# l = 0
# r = len(str_int)-1
# str_int[0] = 1
# while (l <= r):
#     str_int[l], str_int[r] = str_int[r], str_int[l]
#     l += 1
#     r -= 1
x = -123
# str_int = str(abs(x))

if (x < 0):
    flg = True
temp = abs(x)
# digit = 0
rem = 0
while (temp != 0):
    digit = temp % 10
    rem = (rem*10)+digit
    temp = temp//10
if (flg == True):
    print(0-rem)
else:
    print(rem)
