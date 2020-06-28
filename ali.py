num = ['aaa', 'bcd', 'zzz', 'bcdef', 'uvwz', 'bcdefvwzzzzzz', 'bbbb']
n = len(num)
num = sorted(num)
dp = [0 for _ in range(n)]  # 动态数组
dp[0] = len(num[0])
for i in range(1, n):  # 循环1到n
    for j in range(i, -1, -1):  # 循环i-1到0
        if num[i][0] >= num[j][-1]:  # 判断当前字符  比较这个字符和前面所有字符的最后一位，如果打说明可以拼在一起。
            print(num[i][0])
            print(num[j][-1])
            dp[i] = max(len(num[i]) + dp[j], dp[i])
            # print(len(num[i]))
# print(dp)
print(max(dp))



