s = "aaabb"
k = 2

def generate_freq_dict(s):
    temp = {}
    for i in s:
        if(i not in temp):
            temp[i] = 1
        else:
            temp[i] = temp[i]+1
    return temp       


def check(temp:dict,k):
    val = 0
    max = 0
    for value in temp.values():
        if(value>=k):
           val += value 
    return(val)


max = 0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        print(f"{s[i:j]} ------------- {generate_freq_dict(s[i:j])}")
        temp = generate_freq_dict(s[i:j])
    
        if(check(temp,k)>max):
            max = check(temp,k)

print(max)