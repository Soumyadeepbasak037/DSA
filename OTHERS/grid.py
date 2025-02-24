matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
temp = []


def binary_search(arr, low, high, x):

    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:

        return -1


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        temp.append(matrix[i][j])
        # print(matrix[i][j], end=" ")

ind = binary_search(temp, 0, len(temp), target)
print(ind)
