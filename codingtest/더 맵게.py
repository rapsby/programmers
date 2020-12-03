import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        sum_sc = min1 + min2 * 2
        heapq.heappush(scoville, sum_sc)
        answer += 1
    return answer