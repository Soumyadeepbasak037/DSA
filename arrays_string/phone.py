phone_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
              6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

given_digits = "235"

for digit in given_digits:
    string_1 = phone_dict
    print(phone_dict[int(digit)])


temp = []
for i in "abc":
    for j in "def":
        temp = []
        temp.append(i)
        temp.append(j)
        print(temp)
