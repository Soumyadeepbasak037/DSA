tokens = ["18"]


# def eval(op, a, b):
#     if op == "+":
#         return a+b
#     elif op == "-":
#         return a-b
#     elif op == "*":
#         return a*b
#     elif op == "/":
#         return a//b


stack = []
for i in tokens:
    # print(stack)
    if i.lstrip('-').isnumeric():
        stack.append(i)
    else:
        b = int(stack.pop())
        a = int(stack.pop())

        if i == "+":
            stack.append(a+b)
        elif i == "-":
            stack.append(a-b)
        elif i == "*":
            stack.append(a*b)
        else:
            stack.append(a/b)

print(int(stack.pop()))
