#！/usr/bin/python3
#Author:pliu

# class Solution:
#     """
#     动态规划
#     时间复杂度:O(mxn)、空间复杂度O(mxn)
#     """
#     def minDistance(self, word1: str, word2: str) -> int:
#         m = len(word1)
#         n = len(word2)
#         dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
#         # 初始化
#         for i in range(m + 1):
#             dp[i][0] = i
#         for i in range(n + 1):
#             dp[0][i] = i
#         # 状态转移
#         # i , j 代表 word1, word2 对应位置的 index
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 # 此处相当于将w1和w2最后一位相同的字符去掉，比较两者的前面的字符
#                 if word1[i - 1] == word2[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 # 否则从三种状态中选一个最小的然后 +1
#                 else:
#                     dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
#         return dp[m][n]
class Solution:
    """
    BFS
    """
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        q, d, visited = [(0, 0)], 0, set((0, 0))
        while True:
            next = []
            for (w1, w2) in q:
                if word1[w1:] == word2[w2:]:
                    return d
                while w1 < m and w2 < n and word1[w1: w1 + 1] == word2[w2: w2 + 1]:
                    w1 += 1
                    w2 += 1
                if w2 < n and (w1, w2 + 1) not in visited:
                    next.append((w1, w2 + 1))
                    visited.add((w1, w2 + 1))
                if w1 < m and (w1 + 1, w2) not in visited:
                    next.append((w1 + 1, w2))
                    visited.add((w1 + 1, w2))
                if w1 < m and w2 < n and (w1 + 1, w2 + 1) not in visited:
                    next.append((w1 + 1, w2 + 1))
                    visited.add((w1 + 1, w2 + 1))
            q = next
            d += 1


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1,word2))