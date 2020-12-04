from itertools import product
def solution(monster, S1, S2, S3):
    l1 = list(range(1, S1+1))
    l2 = list(range(1, S2+1))
    l3 = list(range(1, S3+1))
    prod = list(map(sum,product(l1, l2, l3)))
    cnt = 0
    for p in prod:
        if p + 1 in monster and p <= S1 + S2 + S3 + 1:
            cnt += 1
    return int((len(prod)-cnt)/len(prod)*1000)

monster = [4, 9, 5, 8]
S1 = 2
S2 = 3
S3 = 3
print(solution(monster, S1, S2, S3))