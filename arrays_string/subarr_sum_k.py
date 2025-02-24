nums = [1,2,3]
k = 3
count = 0
add = 0
for i in range(len(nums)):
    temp = []
    add = 0
    for j in range(i,len(nums)):
        temp.append(nums[j])
        print(temp)
        add+=temp[-1]
        print(add)
        if add == k:
            count +=1
    # print(temp)
print(count)

