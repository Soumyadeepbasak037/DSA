s = "abbccccd"
#Output: ["a","b","bc","c","cc","d"]

segment_list = []


for i in range(len(s)):
    for j in range(i+1,len(s)):
        print(s[i:j])