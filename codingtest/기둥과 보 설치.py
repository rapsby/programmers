def stable(wall):
    for i in range(len(wall)+1):
        for j in range(len(wall)+1):
            if wall[i][j] == 0:
                continue
            if wall[i][j] and 1:
                if 
                pass
            if wall[i][j] and 2:
                if i != 0:
                    if wall[i-1][j] and 1 != 0:
                        if not (j-1 >= 0 and wall[i][j-1] and 2):
                            if not (j+1 <= len(wall) and wall[i][j+1] and 2):
                                return False
    return True
#보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
#기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
    return True
def solution(n, build_frame):
    wall = [[[0] * (n+1)] for _ in range(n+1)]
    for x, y, crossbeam, install in build_frame:
        y = n-y
        if crossbeam:
            wall[y][x] += install
            if not stable(wall):
                wall[y][x] -= install
        else:
            wall[y][x] += 2 * install
            if not stable(wall):
                wall[y][x] -= 2 * install

    answer = [[]]
    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	
#print(solution(n, build_frame))

print(3 and 2)