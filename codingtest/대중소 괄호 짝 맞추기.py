def solution(s):
    d = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    stack = []
    for c in s:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if stack:
                top = stack.pop()
                if d[c] != top:
                    return False
            else:
                return False
    return len(stack) == 0
