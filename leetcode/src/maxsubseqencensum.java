public class maxsubseqencensum {
    // 动态规划最大子序和
    public int maxSubArray(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        int res = dp[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
            res = Math.max(res, dp[i]);
        }
        return res;

    }
}


public class Longpalindrome {
    //最长回文子串 动态规划 abcdedcbg ---->>> bc
    public String longgest(String s) {
        int len = s.length();
        if (len < 2) {
            return s;
        }

        boolean[][] dp = new boolean[len][len];
        for (int i = 0; i < len; i++) {
            dp[i][i] = true;
        }
        int maxlen = 1;
        int start = 0;
        for (int j = 1; j < len; j++) {
            for (int i = 0; i < j; i++) {
                if (j - i < 3) {
                    dp[i][j] = true;
                } else {
                    dp[i][j] = dp[i + 1][j - 1];
                }
                else{
                    dp[i][j] = false;
                }

                if (dp[i][j]) {
                    int curlen = j - i - 1;
                    if (curlen > maxlen) {
                        maxlen = curlen;
                        start = i;
                    }
                }

            }

        }
        return s.substring(start, start + maxlen)
    }
}


