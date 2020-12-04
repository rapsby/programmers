def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x: x*4, reverse=True)
    answer = ''.join(numbers)
    answer = str(int(answer))
    return answer