arr =  [3, 8, 5, 7, 6]

sorted_arr = sorted(arr)

print(sorted_arr)
max  = 0



for i in range(len(sorted_arr)):
    temp_arr = [sorted_arr[i]]
    curr_max=0
    for j in range(i+1,len(sorted_arr)):
        if(temp_arr[-1]+1==sorted_arr[j]):
            temp_arr.append(sorted_arr[j])
            curr_max = len(temp_arr)
            if(curr_max>=max):
                max = curr_max
        print(temp_arr)
print(max)