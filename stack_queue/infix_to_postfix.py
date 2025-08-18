def precedence(op):
    if op in ["*", "/"]:
        return 1
    elif op in ["+", "-"]:
        return 0
    return -1  # for "("

def infix_to_postfix(expr):
    op = ["/", "*", "+", "-"]
    output = []
    op_stack = []
    for i in expr:
        if i == " ":  
            continue
        
        if i in op:
            if not op_stack:
                op_stack.append(i)
            elif precedence(i) > precedence(op_stack[-1]):
                op_stack.append(i)
            else:
                while (op_stack and op_stack[-1] != "(" 
                       and precedence(op_stack[-1]) >= precedence(i)):
                    output.append(op_stack.pop())
                op_stack.append(i)
                
        elif i == "(":
            op_stack.append(i)

        elif i == ")":
            while op_stack and op_stack[-1] != "(":
                output.append(op_stack.pop())
            if op_stack:  
                op_stack.pop()

        else:
            output.append(i)
    
    while op_stack:
        output.append(op_stack.pop())

    print(output)
    print(op_stack)

infix_to_postfix("(A+B)*(C-D)-E/F")

def eval_symbol(op1,op2,symbol):
    if(symbol == "+"):
        return op1+op2
    if(symbol == "-"):
        return op2-op1
    if(symbol == "*"):
        return op1*op2
    if(symbol == "/"):
        return op2/op1
    

def eval_postfix(expr):
    op = ["/", "*", "+", "-"]
    stack = []
    for i in expr:
        if(i in op):
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.append(eval_symbol(operand_1,operand_2,i))
        else:
            stack.append(int(i))

    return stack.pop()
    
postfix_expr = ["2", "3", "+", "4", "1", "-", "*"]
print(eval_postfix(postfix_expr))  
