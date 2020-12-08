def stable(constructure):
    for x, y, crossbeam in constructure:
        if crossbeam:
            if (x, y-1, 0) in constructure or (x+1, y-1, 0) in constructure or ((x-1, y, 1) in constructure and (x+1, y, 1) in constructure):
                continue
            else:
                return False
        else:
            if y == 0 or (x-1, y, 1) in constructure or (x, y, 1) in constructure or (x, y-1, 0) in constructure:
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = set()
    for x, y, crossbeam, install in build_frame:
        if install:
            answer.add((x, y, crossbeam))
            if not stable(answer):
                answer.remove((x, y, crossbeam))
        else:
            answer.remove((x, y, crossbeam))
            if not stable(answer):
                answer.add((x, y, crossbeam))
    answer = list(map(list,answer))
    answer.sort()
    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	
print(solution(n, build_frame))
