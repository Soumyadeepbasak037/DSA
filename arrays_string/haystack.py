haystack = "mississippi"
needle = "issip"
counter = 0
temp = 0
flag = False
i = 0
temp2 = 0

while (i in range(len(haystack))):
    if flag == True:
        break
    if (counter != len(needle) and haystack[i] == needle[counter]):
        # print(i, counter)
        if (counter == len(needle)-1):
            flag = True
            temp = i-(len(needle)-1)
        counter += 1    
    else:
        counter = 0
    i += 1

if flag == True:
    print(temp)
else:
    print(-1)
