import heapq
def solution(n, works):
    if n >= sum(works):
        return 0
    works = [-i for i in works]
    heapq.heapify(works) 
    for _ in range(n):
        w = heapq.heappop(works) + 1
        heapq.heappush(works, w)
    return sum([i**2 for i in works])

n = 10
works = [4,3,3,5,12,15]
print(solution(n, works))