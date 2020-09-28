from torch import nn


def func(array):
    """
    网易数据挖掘笔试题
    :param array:
    :return:
    """
    size = len(array)
    res = [0] * size
    for i in range(0, size - 1):
        for j in range(i, size):
            if (array[j] < array[i]):
                res[i] = j - i
                break
            else:
                res[i] = 0
    res = ",".join(str(i) for i in res)
    return res


"""
最长无重复的子串
"""


def lengthsubstring(s):
    occ = set()
    n = len(s)
    right = -1
    ans = 0
    for i in range(n):
        if n != 1:
            occ.remove(s[i - 1])
        while right + 1 < n and s[right + 1] not in occ:
            occ.add(s[right + 1])
            right += 1
        ans = max(ans, right - i + 1)


def countsubString(s):
    """
    回文子串的个数
    :param s:
    :return:
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0
    for j in range(n):
        for i in range(0, j + 1):
            length = j - i + 1
            if length == 1:
                dp[i][j] = True
                count += 1
            if length > 2 and s[i] == s[j] and dp[i + 1][j - 1] is True:
                dp[i][j] = True
                count += 1
    return count // 2


# s = input()
# res = countsubString(s)
# print(res)
""" 
def findlength(s):
    """
找
a, b, c, x, y, z
都恰好出现偶数次的最长字符串
:param
s:
:return:

dp = [-float('inf')] * 32
dp[0] = -1
pattern = 0
res = 0
for i in range(len(s)):
    if s[i] == 'a':
        pattern ^= (1 << 0)
    elif s[i] == 'b':
        pattern ^= (1 << 1)
    elif s[i] == 'c':
        pattern ^= (1 << 2)
    elif s[i] == 'x':
        pattern ^= (1 << 3)
    elif s[i] == 'y':
        pattern ^= (1 << 4)
    elif s[i] == 'z':
        pattern ^= (1 << 5)
    if dp[pattern] != -float('inf'):
        cur_len = i - dp[pattern]
        res = max(res
                  , cur_len)
    else:
        dp[pattern] = i

return res
