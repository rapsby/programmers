def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ['ICN']
    path = []
    while stack:
        top = stack[-1]
        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        else:
            path.append(stack.pop())
    return path[::-1]

print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
p = {}
p[0] = []
if p[0]:
    print(p[0])
else:
    print(2)