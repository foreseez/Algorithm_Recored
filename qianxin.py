#
import itertools


# 返回亲7数个数
# @param digit int整型一维数组 组成亲7数的数字数组
# @return int整型
#
class Solution:
    def reletive_7(self, digit):
        result = []
        for i in itertools.permutations(digit,len(digit)):
            result.append(i)
            print(result)
        ans = 0
        for num in result :
            if (num % 7)== 0:
                ans += 1
        return ans



