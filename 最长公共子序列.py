def longgest(str1,str2):
    m,n = len(str1,str2)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

import numpy as np 
arr = np.zeros([2,2])
print(arr)

