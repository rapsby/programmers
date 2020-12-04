def solution(skill, skill_trees):
    d = {}
    for i, s in enumerate(skill):
        d[s] = i
    cnt = 0
    for sk in skill_trees:
        stack = []
        flag = True
        for s in sk:
            if s in d:
                if stack and stack[-1] + 1 == d[s]:
                    stack.append(d[s])
                elif not stack and d[s] == 0:
                    stack.append(d[s])
                else:
                    flag = False
                    break
        if flag:
            cnt += 1
    return cnt

print(solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA']))