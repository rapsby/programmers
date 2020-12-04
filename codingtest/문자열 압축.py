def solution(s):
    answer = []
    string = ''
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        cnt = 1
        head = s[:i]
        for j in range(i, len(s), i):
            if head == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                string += str(cnt) + head
                head = s[j:j+i]
                cnt = 1
        if cnt == 1:
            cnt = ''
        string += str(cnt) + head
        answer.append(len(string))
        string = ''
    return min(answer)

print(solution('aabbaccc'))