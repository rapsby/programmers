def solution(participant, completion):
    d = {}
    
    for p in participant:
        # d.get(p, 0) -> if p in d: return d[p] else: return 0
        d[p] = d.get(p, 0) + 1

    for c in completion:
        if d[c] == 1:
            del d[c]
        else:
            d[c] -= 1
    
    return list(d)[0]