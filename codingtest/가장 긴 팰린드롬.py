def isPalindrome(s):
    return s == s[::-1]
def solution(s):
    if len(s) <= 1:
        return len(s)
    i,l=0,0
    for j in range(len(s)):
        print(j,i,l, s[i:l])
        if isPalindrome(s[j-l: j+1]):
            print(1)
            i, l = j-l, l+1
            print(s[i:i+l])
        elif j-l > 0 and isPalindrome(s[j-l-1: j+1]):
            print(2)
            i, l = j-l-1, l+2
            print(s[i:i+l])
        print('>',j,i,l, s[i:i+l])
        
    return len(s[i: i+l])
print(solution('abcdcba'))