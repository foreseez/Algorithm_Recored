"""阿里笔试题"""
def solve(s):
    s.sort()
    dp = [0 for i in range(len(s))]
    dp[0] = len(s[0])
    for i in range(0,len(s)):
        for j in range(i + 1, len(s)):
            if s[j][0] > s[i][-1] and dp[i] + len(s[j]) > dp[j]:
                dp[j] = dp[i] + len(s[j])
    return dp[len(s) - 1]
s = ['aaaaaaa', 'bcd', 'zzz', 'bcdef', 'uvwz', 'bcdefvwzzzzzz', 'bbbb', 'bbbbu']
print(solve(s))