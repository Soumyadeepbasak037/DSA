def isValid(s: str) -> bool:
    # Dictionary to hold the matching pairs
    mapping = {")": "(", "}": "{", "]": "["}
    # Stack to keep track of the opening brackets
    stack = []

    for char in s:
        if char in mapping.values():
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
        elif char in mapping.keys():
            # If it's a closing bracket
            # Check if the stack is not empty and the top of the stack matches the corresponding opening bracket
            if stack and stack[-1] == mapping[char]:
                stack.pop()  # Pop the matching opening bracket
            else:
                return False
        else:
            # Invalid character (not part of the defined brackets)
            return False

    # If the stack is empty, all the brackets were matched
    return not stack
