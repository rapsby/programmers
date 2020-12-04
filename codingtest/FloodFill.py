from collections import deque
def solution(n, m, image):
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    dir = [[1,0], [0,1], [-1,0], [0,-1]]
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                q = deque()
                q.append([i,j])
                visited[i][j] = True
                color = image[i][j]
                while q:
                    y, x = q.popleft()
                    for dy, dx in dir:
                        yy, xx = y+dy, x+dx
                        if 0 <= yy < n and 0 <= xx < m:
                            if not visited[yy][xx]:
                                if image[yy][xx] == color:
                                    visited[yy][xx] = True
                                    q.append([yy,xx])
                cnt += 1
    return cnt

print(solution(2,3, [[1, 2, 3], [3, 2, 1]]))