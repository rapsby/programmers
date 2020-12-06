from copy import copy, deepcopy
def rotate(key):
    return [list(reversed(i)) for i in zip(*key)]

def isMatch(lock, n, m):
    for i in lock[m-1:-(m-1)]:
        for j in i[m-1:-(m-1)]:
            if j != 1:
                return False
    return True

def insert(y, x, key, lock, n, m):
    for dy in range(m):
        for dx in range(m):
            lock[y+dy][x+dx] += key[dy][dx]
            if lock[y+dy][x+dx] == 2:
                return False
    return isMatch(lock, n, m)

def check(lock, key, n, m):
    for _ in range(4):
        for y in range(n+m-1):
            for x in range(n+m-1):
                copied_lock = deepcopy(lock)
                if insert(y,x, key, copied_lock, n, m):
                    return True
        key = rotate(key)
    return False

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(m-1) + l + [0]*(m-1) for l in lock]
    new_lock = [[0] * (2*(m-1)+n) for _ in range(m-1)] + new_lock + [[0] * (2*(m-1)+n) for _ in range(m-1)]
    return check(new_lock, key, n, m)


key = [[0, 1, 1], [0, 1, 1], [1, 0, 1]]	
lock = [[1, 1, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]]	

#key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
#lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
print(solution(key, lock))