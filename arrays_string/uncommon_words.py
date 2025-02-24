s1 = "this apple is sweet"
s2 = "this apple is sour"
flag = 0

for i in range(min(len(s1), len(s2))):
    if (s1[i] != s2[i]):
        flag = i
print(flag)
