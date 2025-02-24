temperatures = [73,74,75,71,69,72,76,73]

for i in range(len(temperatures)):
    for j in range(i+1,len(temperatures)):
        # print(i,j)
        if(temperatures[j]>temperatures[i]):
            print(temperatures[i],temperatures[j])