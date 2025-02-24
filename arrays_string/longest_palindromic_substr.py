s = "aacabdkacaa"


def check_palindrome(arr):
    temp = ''
    for i in range(len(arr)-1, -1, -1):
        temp += (arr[i])
    if (temp == arr):
        return True
    else:
        return False


def check_palindrome_slicing_from_end(s, j):
    flag = False
    for i in range(len(s), 1, -1):
        print(s[j:i])
        if (len(s[j:i]) != 1 and check_palindrome(s[j:i]) == True):
            flag = True
            print("The substr is: ", s[j:i], " with j,i:", j, i)
            break
    if (flag == False):
        check_palindrome_slicing_from_end(s, j+1)


check_palindrome_slicing_from_end(s, 0)
# print(s[1:4])
# print(s[1:3])
