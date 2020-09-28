# def subarraysum(nums, k):
#     sum = [0] * len(nums)
#     sum[0] = nums[0]
#     for i in range(1, len(nums)):
#         sum[i] = sum[i - 1] + nums[i]
#     for i in range(0, len(nums)):
#         for j in range(i, len(nums)):
#             sum_new = sum[j] - sum[i] + nums[i]
#             if sum_new == k:
#                 return True
#     return False
#
#
# nums = [1, 3, 5, 7, 9]
# k = 7
# res = subarraysum(nums, k)
# print(res)


def maxarea(array):
    area = 0
    for i in range(1, len(array) - 1):
        left_length = max(array[0:i])
        right_length = max(array[i + 1:-1])
    area = min(left_length, right_length) * 2
    return area
#2,1,2,1
#4*1=4

def maxarea2(array):
    maxarea = 0
    m = len(array)
    n = len(array[0])
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(1,m):
        for j in range(1,n):
            if array[i-1][j-1] = "0":
                continue
            width = dp[i][j] = dp[i][j] +1 if j else 1
            for k in range(i,-1,-1):
                width = min(width,dp[k][j])
                maxarea = max(maxarea,width*(i-k))
    return maxarea  o(n*n*m)

            