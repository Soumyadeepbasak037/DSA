info = 123456
act = "RLTDRRTRS2S1"

# output = 244156
arr = []
counter = 0

for i in str(info):
    arr.append(int(i))
print(arr)


def swap(arr: list, num1, num2):
    temp = arr[num1]
    arr[num1] = arr[num2]
    arr[num2] = temp
    print(arr)


# swap(arr, 0, 1)

for count, i in enumerate(act):
    if i == "R":
        print("R->Next char")
        counter += 1
        print(arr)
    elif i == "L":
        print("L->Prev char")
        counter -= 1
        print(arr)
    elif i == "T":
        print("T->Increment by 1")
        arr[counter] = (arr[counter]+1)
        print(arr)
    elif i == "D":
        print("D->Decrement by 1")
        arr[counter] = (arr[counter]-1)
        print(arr)
    elif i == "S":
        print("S-> Swapping")
        req = int(act[count+1])
        swap(arr, counter, req-1)
 