s = "3[a]2[bc]"
stack = []

for i in s:
    if (i.isnumeric or i == "["):
        stack.append(i)
    else:
        while stack and stack[-1] != "[":
            alpha = stack.pop()
        stack.pop()
    num = stack.pop()
    stack.append(num*alpha)
print(stack)
