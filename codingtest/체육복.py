def solution(n, lost, reserve):
    # 앞뒤에 패딩 삽입
    u = [1] * (n + 2)
    for r in reserve:
        u[r] += 1
    for l in lost:
        u[l] -= 1
    for i in range(1, n + 1):
        if u[i-1] == 0 and u[i] == 2:
            u[i-1], u[i] = 1, 1
        elif u[i] == 2 and u[i+1] == 0:
            u[i], u[i+1] = 1, 1
    
    return len(u) - 2 - u.count(0)

def solution2(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    for i in sorted(r):
        if i - 1 in l:
            l.remove(i - 1)
        elif i + 1 in l:
            l.remove(i + 1)
    return n - len(l)

