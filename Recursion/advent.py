# arr = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
cur = 50
count = 0


import sys

arr = []
for line in sys.stdin:
    line = line.strip()
    if line:
        arr.append(line)



for i in range(len(arr)):
    temp = 0
    ins = arr[i][0]
    num = int(arr[i][1:])
    if(ins == 'L'):
        temp = cur - num
        cur = temp % 100
    if(ins == 'R'):
        temp = cur + num
        cur = temp % 100
    
    if(temp>99):
    elif9tem

    

        
    if(cur == 0):
        count+=1
    print(f"{arr[i]}:{cur},count:{count}")