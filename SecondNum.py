def secondenum(nums):
    """
    求第二小数字
    :param nums:
    :return:
    """
    Maxnum = max(nums)
    Secondnum = float('-Inf')
    for num in nums:
        if num > Secondnum and num < Maxnum:
            Secondnum = num
    return Secondnum


a = list(filter(lambda x: x % 2 == 1, [1, 23, 4, 5, 65, 6, 7, 78, 8, 8, ]))
print(a)

nums = [1, 23, 4, 5, 65, 6, 7, 78, 8, 8, ]
res = secondenum(nums)
print(res)
print("===============")
import time
from functools import wraps


# def log(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         ret = func(*args, **kwargs)
#         end = time.perf_counter()
#         print("start:%s, end:%s, 耗时%s" % (start, end, end - start))
#         return ret
#
#     return wrapper
#
#
# @log
# def foo():
#     print('xxxxxx')
# foo()

def addition(func):
    @wraps(func)
    def wrapper(a, b):
        res = a + b
        return res

    return wrapper


@addition
def add():
    print("add res")


add(988, 777)

"""
简易的快排
"""


def quick_sort(array):
    if len(array) == 0:
        return array
    else:
        pivot = array[0]
        left_part = [x for x in array if x < pivot]
        right_part = [x for x in array if x > pivot]
        array = quick_sort(left_part) + [pivot] + quick_sort(right_part)
    return array


arr = [1, 5, 7, -2, -3, 10, 3, 200, -300, 1000, -30]
print(quick_sort(arr))


def Bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


"""
从左上角到右下角有多少种路径
C(m+n-2,m-1)
排列组合问题
"""


def sumpath(m,n):
    dp = [[0 for i in range(m)] for _ in range(n)]
    dp[0][0] = 0
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1,n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
