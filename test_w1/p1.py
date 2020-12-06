def solution(n, words):
    d = {}
    prev = ''
    for i, word in enumerate(words):
        if word in d:
            return [i % n + 1, i // n + 1]
        else:
            if i == 0:
                prev = word[-1]
                d[word] = word
            elif prev != word[0]:
                return [i % n + 1, i // n + 1]
            else:
                prev = word[-1]
                d[word] = word 
    else:
        return [0, 0]

n = 3
words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']	
#n = 2
#words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']	
print(solution(n,words))