def isvalid(s):
    if len(s)%2==1:
        return False
    pairs = {
        ")":"(",
        "]":"[",
        "}":"{"
    }


    stack = list()
    for char in s:
        if char in pairs:
            if not stack and stack[-1] != pairs[char]
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack

