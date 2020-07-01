class Solution:
    '''
    输入的有重复的数字
    这个算法去除了重复的子集
    '''
    def subsetsWithDup(self, nums):
        n = len(nums)
        nums.sort()
        res = [[]]
        pre = []
        for i in range(n):
            if (i>0 and nums[i] == nums[i-1]):
                pre = [tmp + [nums[i]] for tmp in pre]
            else:
                pre = [tmp+[nums[i]] for tmp in res]
            res += pre
        return res


func = Solution()
nums = [1,2,2,3]
result = func.subsetsWithDup(nums)
print(result)




class Solution2:
    '''
    结果有重复的子集
    '''
    def subsetsWithDup(self, nums):
        n = len(nums)
        nums.sort()
        res = [[]]
        pre = []
        for i in range(n):
            #if (i>0 and nums[i] == nums[i-1]):
             #   pre = [tmp + [nums[i]] for tmp in pre]
            #else:
            pre = [tmp+[nums[i]] for tmp in res]
            res += pre
        return res

func2 = Solution2()    #alt +shift+上下  移动
nums = [1,2,2,3]
result2 = func2.subsetsWithDup(nums)
print(result2)

"""
[[], [1], [2], [1, 2], [2, 2], [1, 2, 2], [3], [1, 3], [2, 3], [1, 2, 3], [2, 2, 3], [1, 2, 2, 3]]
[[], [1], [2], [1, 2], [2], [1, 2], [2, 2], [1, 2, 2], [3], [1, 3], [2, 3], [1, 2, 3], [2, 3], [1, 2, 3], [2, 2, 3], [1, 2, 2, 3]]


"""


