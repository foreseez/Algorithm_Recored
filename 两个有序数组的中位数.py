"""

两个有序数组的中位数

"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        infinty = 2 ** 40
        m, n = len(nums1), len(nums2)
        left, right, ansi = 0, m, -1
        # median1：前一部分的最大值
        # median2：后一部分的最小值
        median1, median2 = 0, 0

        while left <= right:
            # 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
            # // 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            nums_im1 = (-infinty if i == 0 else nums1[i - 1])
            nums_i = (infinty if i == m else nums1[i])
            nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
            nums_j = (infinty if j == n else nums2[j])

            if nums_im1 <= nums_j:
                ansi = i
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1

        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1


"""
最长回文串
给定一些字母输出 能够组成的最长回文串

"""


class Solution:
    def longestPalindrome(self, s):
        ans = 0
        count = collections.Counter(s)  # 统计每个字母出现的次数  一个字母最多可以使用 2 * （次数 // 2）
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:  # 如果是奇数的话放在偶数次字母的最中间
                ans += 1
        return ans

"""
Java 合并有序数组
"""
class Solution {
    public void merge(int[] A, int m, int[] B, int n) {
        int k = m+n-1;
        int i = m-1;
        int j = n-1;
        while(i>=0&&j>=0){
            if(A[i] < B[j]){
                A[k--] = B[j--];
            }else{
                A[k--] = A[i--];
            }
        }
        while(j>=0)
        A[k--] = B[j--];
    }
}
