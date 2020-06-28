# class Solution:
#     def generateParenthesis(self, n):
#         ans = []
#         def backtrack(S, left, right):
#             if len(S) == 2 * n:
#                 ans.append(''.join(S))
#                 return
#             if left < n:
#                 S.append('(')
#                 backtrack(S, left+1, right)
#                 S.pop()
#             if right < left:
#                 S.append(')')
#                 backtrack(S, left, right+1)
#                 S.pop()
#
#         backtrack([], 0, 0)
#         return ans
class Solution:
    def generateParenthesis(self, n):
        dp = [[] for _ in range(n + 1)]  # dp[i]存放i组括号的所有有效组合pr
        dp[0] = [""]  # 初始化dp[0]
        for i in range(1, n + 1):  # 计算dp[i]
            for p in range(i):  # 遍历p
                l1 = dp[p]  # 得到dp[p]的所有有效组合
                l2 = dp[i - 1 - p]  # 得到dp[q]的所有有效组合
                for k1 in l1:
                    for k2 in l2:
                        print(k1,k2)
                        dp[i].append("({0}){1}".format(k1, k2))

        return dp[n]

if __name__ == '__main__':
    t = Solution().generateParenthesis(3)
    print(t)

