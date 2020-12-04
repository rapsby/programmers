def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack and stack.pop() == '(':
                continue
            else:
                return False
    return len(stack) == 0