"""最长无重复子串"""
"""判断是否有重复字符"""
"""滑动窗口 一次向右枚举每个起始位置的最长子串，right 表示不重复的最长子串结束位置"""


class Solution:
    def length(self, s: str) -> int:
        occ = set()
        n = len(s)
        right, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一格字符
                occ.remove(s[i - 1])
                while right + 1 < n and s[right + 1] not in occ:
                    # 移动右指针
                    occ.add(s[right + 1])
                    right += 1
            ans = max(ans, right - i + 1)
        return ans


'''
for sentence ,lable in sentences:
    senntence = [word2id_dict[word] if word in word2id_dict else word2id_dict[['oov']] for word in sentence]
'''


# 岛屿的个数，先把1周围的1变成0
class Solution_island:
    def numofisland(self, array):
        row = len(array)
        count = 0
        colm = len(array[0])
        for i in range(row):
            for j in range(colm):
                if array[i][j] == '1':
                    count += 1
                    self.recurse(array, i, j)
        return count

    def recurse(self, array, l, h):
        array[l][h] == '0'
        if l - 1 > 0 and array[l - 1][h] == '1':
            self.recurse(array, l - 1, h)
        if l + 1 < len(array) and array[l + 1][h] == '1':
            self.recurse(array, l + 1, h)
        if h - 1 > 0 and array[l][h - 1] == '1':
            self.recurse(array, l, h - 1)
        if h + 1 < len(array[0]) and array[l][h + 1] == '1':
            self.recurse(array, l, h + 1)


class PrintTreeParth:
    def __init__(self,left,right,val):
        self.left = None
        self.right = None
        self.val = val
    def constructPath(self,root:TreeNode,path):
        paths = []
        if root:
            path += str(root.val)
            if not root.left and root.right:  #当前节点是叶子节点
                paths.append(path)
        else:
                self.constructPath(root.left,path) #不是叶子节点
                self.constructPath(root.right,path)


