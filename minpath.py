def minpath(array):
    m = len(array)
    n = len(array[0])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = array[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + array[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + array[0][j]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + array[i][j]
    return dp[-1][-1]





"""
7.3 日面试字节后端提前批一面
二维非负数组，每次只能向右或者向下走，
寻找从 [0, 0] -> [i, j] 
的最短路径（数字相加最小），
返回对应值。




"""
"""

select name 
from tabble 
group by id,name 
having min(score) >60

"""