def rev_arr(arr, l, r):
    if (l >= r):
        return

    arr[l], arr[r] = arr[r], arr[l]
    rev_arr(arr, l+1, r-1)


arr = [1, 2, 3, 4, 5]
rev_arr(arr, 0, len(arr)-1)
print(arr)
