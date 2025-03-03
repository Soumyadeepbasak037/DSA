s = "100[leetcode]"
# stack = []
# accum = []
# for i in s:
#     if (i!="]"):
#         stack.append(i)
#         # print(stack)
#     else:
#         res = []
#         while stack and stack[-1] != '[':
#             alpha = stack.pop()
#             res.insert(0, alpha)
#             print(res)
#             accum.append(res)
#     #     stack.pop()
#     # num = stack.pop()
# #     stack.append(num*alpha)
# # print(stack)

# print(accum)


stack = []
for char in s:
    if char != "]":
        stack.append(char)
    else:
        substr = ""
        while stack and stack[-1] != "[":
            substr = stack.pop()+substr
        stack.pop()

        num = ""
        flag = False
        while stack and stack[-1].isdigit() or flag == True:
            num += stack.pop()
            print(num)
            if (stack and stack[-1].isdigit):
                flag == True

        rev = ''.join(reversed(num))
        # print(rev)
        stack.append(int(rev) * substr)

res = "".join(stack)
print(res)
