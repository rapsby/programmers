def solution(board, nums):
    n = len(board)
    nums = dict.fromkeys(nums)
    row_list = [0] * n
    col_list = [0] * n
    line1 = 0
    line2 = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] in nums:
                board[i][j] = 0
                row_list[i] += 1
                col_list[j] += 1
                if i == j:
                    line1 += 1
                if n - 1 - i == j:
                    line2 += 1
    answer = line1//n + line2//n
    answer += sum([1 for i in row_list if i == n])
    answer += sum([1 for i in col_list if i == n])
    return answer