from queue import PriorityQueue
def solution(N, road, K):
    q = PriorityQueue()
    q.put([1, 0])
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    while not q.empty():
        current, current_cost = q.get()
        for src, dest, cost in road:
            next_cost = cost + current_cost
            if src == current and next_cost < dist[dest]:
                dist[dest] = next_cost
                q.put([dest, next_cost])
            if dest == current and next_cost < dist[src]:
                dist[src] = next_cost
                q.put([src, next_cost])
    return len([i for i in dist if i <= K])

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))