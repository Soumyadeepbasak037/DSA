s = "3+2*2"
stack = []

for i in s:
    stack.append(i)


# print(stack)
# stack.pop()
# stack.pop()
# print(stack)

a = 0
b = 0
while len(stack)>1:
    if(isinstance(stack[-1],int)):
        a = stack.pop()
    else:
        print(a)
        op = stack.pop()
        b = stack.pop()
        if(op == "*"):
            stack.append(a*b)
        if(op=="+"):
            stack.append(a+b)
print(stack)

    # while(isinstance(stack[-1],int)):
    #     print(stack.pop())