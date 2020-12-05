def solution(n):
    answer = 0
    a = 0
    b = 1
    c = 0
    for i in range(n+1):
        c = b
        b = (a+b) % 1000000007
        a = c

    return c