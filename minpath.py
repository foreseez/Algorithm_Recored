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
统计全为 1 的正方形子矩阵  包含边长为1，2，3.。。。的 
"""
import numpy as np


def countSquare(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = np.zeros(n, m)
    res = 0
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = matrix[i][j]
            elif matrix[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            res += dp[i][j]
    return res


"""
二叉树的中序遍历 非递归

"""
def inorder(root):  #中序递归
    if root is None:
        return None
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def inorder1(root): #中序非递归
    stack = []
    cur  = root
    res  = []
    while cur or stack is not None:
        if cur is not None:
            stack.push(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            print(cur.val)  #res.append(cur.val)
            cur = cur.right
    return res

import  queue

def level(root):
    if root is None:
        return None
    res = []
    que = queue
    if root :
        que.add(root)
    while que:
        n = len(que)
        level = []
        for i in range(n): #遍历完每层的元素
            node = que.popleft() # 只想队列的最左边   队列右进左出 节点出队列的时候把它的左右节点入队。
            level.add(node.val)
            if(node.left is not None):
                que.add(node.left)
            if (node.right is not None):
                que.add(node.right)
        res.add(level)
    return res




