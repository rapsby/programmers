def solution(dirs):
    visited = dict()
    y, x = 0, 0
    for d in dirs:
        if d == 'U' and y < 5:
            visited[(y, x, y+1, x)] = True
            y += 1
        elif d == 'D' and y > -5:
            visited[(y, x, y-1, x)] = True
            y -= 1
        elif d == 'R' and x < 5:
            visited[(y, x, y, x+1)] = True
            x += 1
        elif d == 'L' and x > -5:
            visited[(y, x, y, x-1)] = True 
            x -= 1
    return len(visited)

print(solution('ULURRDLLU'))