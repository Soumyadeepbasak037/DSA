chalk = [1, 1, 1]
k = 2


i = 0
while k >= 0:
    # print(chalk[i])
    print(k)
    k -= chalk[i]
    if (i != len(chalk)-1):
        i += 1
    else:
        i = 0
# print(k)
print("I: ", i - 1)
