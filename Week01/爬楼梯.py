import functools
class Solution:
    """
    解题方法：1、利用F(n) = F(n-1) +F(n-2)递归，时间复杂度O(n^2)。递归
             2、在1的基础上，将计算过的缓存下来，下次碰到就不在计算，直接从缓存中拿。递归+记忆化搜索。时间复杂度O(n),空间复杂度O(n)
             3、动态规划，既递推。后面的将前一个覆盖。时间复杂度O(n)、空间复杂度O(1)
             4、矩阵快速幂或通向公式。时间复杂度O(logn)
    """
    @functools.lru_cache(100)  # 缓存装饰器
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
a = 3
print(Solution().climbStairs(a))



