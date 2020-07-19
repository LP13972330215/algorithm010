class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        思路：text1和text2的公共最长子序列为lcs，某个字符要么在lcs，要么不在。
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        # 初始化DP tables,生成一个（m+1）*（n+1)的全0二维矩阵。多创建的第一行和第一列是为了不越界。
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]: #相等，则将i、j往前移动1，且lcs+1
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])#不相等，则取上面和左边的最大值
        return dp[-1][-1]

