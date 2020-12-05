import time

from collections import deque
stack = []
def bfs(board, y, x, path) :
    cnt = 0
    queue = deque()
    dir = [[1,0], [0,1], [-1,0], [0,-1]]
    queue.append((y, x))
    while queue :
        y, x = queue.popleft()
        for dy, dx in dir:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
                if board[ny][nx] == 0:
                    continue
                if board[ny][nx] == 1:
                    queue.append((ny, nx))
                    path.append((ny, nx))
                    board[ny][nx] = board[y][x]+1
                    n_path, _ = bfs(board, ny, nx, path)
                    if len(n_path) < len(path):
                        path = n_path
                        cnt = 1
                    elif len(n_path) == len(path):
                        cnt += 1
    return path, cnt

def solution(m, n, puddles):
    board = [[1] * m for _ in range(n)]
    for x, y in puddles:
        board[y-1][x-1] = 0

    for i in board:
        print(i)
    board[0][0] = 0
    print(bfs(board, 0, 0, []))

m = 5
n = 5
puddles = [[2,2],[4,2],[1,3]]
print(solution(m, n, puddles))