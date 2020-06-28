class Solution(object):
    def myPow(self, x, n):
        """
        二分求幂
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n:
            if n % 2:
                ans *= x
            n >>= 1# 往右边移1位，相当于除2取整数
            x *= x
        return ans

# class Solution(object):
#     def myPow(self, x, n):
#         """
#         时间复杂度O(1)，空间复杂度O(1)
#         :type x: float
#         :type n: int
#         :rtype: float
#         """
#         if n == 0:
#             return 1
#         if n < 0:
#             print(1111)
#             x = 1 / x
#             n = -n
#         print(n,x)
#         if n % 2:
#             print('递归',n)
#             return x * self.myPow(x, n - 1)
#
#         return self.myPow(x * x, n / 2)

if __name__ == '__main__':
    print(Solution().myPow(2.0,4))
