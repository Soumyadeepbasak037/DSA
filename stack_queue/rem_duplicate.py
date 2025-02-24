s = "leetcode"

stack = []

for i in s:
    print(i)
    if i not in stack:
        stack.append(i)


def swap(i, j, arr):
    temp = ""
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# arr = [1, 2, 3, 4]
# swap(0, 3, arr)
# print(arr)

for i in range(len(stack)):
    for j in range(i, len(stack)):
        if (stack[i] > stack[j]):
            temp = ""
            temp = stack[i]
            stack[i] = stack[j]
            stack[j] = temp
            # swap(i, j, stack)

print(stack)
req_str = ""
for i in stack:
    req_str += i
print(req_str)
