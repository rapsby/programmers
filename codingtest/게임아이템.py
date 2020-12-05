from queue import PriorityQueue
def solution(healths, items):
    answer = []
    items = [[item[1], item[0], i+1] for i, item in enumerate(items)]
    items.sort()
    healths.sort()
    pq = PriorityQueue()
    start = 0
    for health in healths:
        for item in items[start:]:
            hp, power, i= item
            if health - hp < 100:
                break
            pq.put((-power, i))
            start += 1
        if not pq.empty():
            _, i = pq.get()
            answer.append(i)
    return sorted(answer)


healths = [200,120,150]
items = [[30,100],[500,30],[100,400]]	

healths = [300,200,500]	
items = [[1000, 600], [400, 500], [300, 100]]	
print(solution(healths, items))