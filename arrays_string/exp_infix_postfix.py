def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0


def infix_to_postfix(exp: str):
    output = []
    op_stack = []

    for char in exp:
        if char.isdigit():
            output.append(char)

        elif char == "(":
            op_stack.append(char)

        elif char == ")":
            while op_stack and op_stack[-1] != "(":
                output.append(op_stack.pop())
            op_stack.pop()
        else:
            while op_stack and precedence(op_stack[-1]) >= precedence(char):
                output.append(op_stack.pop())
            op_stack.append(char)

    while op_stack:
        output.append(op_stack.pop())

    return "".join(output)


def evaluate(a, b, char):
    a = int(a)
    b = int(b)
    if char == "+":
        return a+b
    elif char == "-":
        return a-b
    elif char == "*":
        return a*b
    else:
        return a/b


def eval_postfix(expr: str):
    stack = []
    for char in expr:
        if char.isdigit():
            stack.append(char)
        else:

            b = stack.pop()
            a = stack.pop()
            stack.append(evaluate(a, b, char))
    return stack[0]


infix_expr = "5+2*(8-3)"
postfix_expr = infix_to_postfix(infix_expr)
print("Postfix:", postfix_expr)  # Output: 5283-*+
print(eval_postfix(postfix_expr))
