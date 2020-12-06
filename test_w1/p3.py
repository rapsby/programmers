from collections import deque

def getNewPos(pos, board):
    dir = [[0,1], [1,0], [0,-1], [-1,0]]
    newPos = []
    y1, x1 = pos[0]
    y2, x2 = pos[1]

    # 상하좌우 이동
    for dy, dx in dir:
        if board[y1+dy][x1+dx] == 0 and board[y2+dy][x2+dx] == 0:
            newPos.append({(y1+dy, x1+dx), (y2+dy, x2+dx)})
    
    # 가로 -> 세로
    if y1 == y2:
        for dy, dx in dir[1::2]:
            if board[y1+dy][x1+dx] == 0 and board[y2+dy][x2+dx] == 0:
                newPos.append({(y1, x1), (y1+dy, x1)})
                newPos.append({(y2, x2), (y2+dy, x2)})

    # 세로 -> 가로
    else:
        for dy, dx in dir[::2]:
            if board[y1+dy][x1+dx] == 0 and board[y2+dy][x2+dx] == 0:
                newPos.append({(y1, x1), (y1, x1+dx)})
                newPos.append({(y2, x2), (y2, x2+dx)})
    return newPos


def solution(board):
    n = len(board)
    board = [[1] + b + [1] for b in board]
    board = [[1] * (n + 2)] + board + [[1] * (n + 2)]
    pos = {(1,1), (1,2)}
    q = deque()
    visited = []
    q.append([pos, 0])
    visited.append(pos)
    while q:
        pos, distance = q.popleft()
        distance += 1
        #print('visited: ', visited)
        for newPos in getNewPos(list(pos), board):
            if (n, n) in newPos:
                return distance
            if newPos not in visited:
                #print(newPos)
                q.append([newPos, distance])
                visited.append(newPos)
    return -1


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	
print(solution(board))