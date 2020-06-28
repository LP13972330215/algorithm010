class Solution:
    '''
    TODO:跑梯子。爬楼梯时，需要n阶你才能达到楼顶。每次可以爬1或2个台阶，有多少种不同的方法可以爬到楼顶。
    空间复杂度为O(1)
    '''
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2: return n
        first, second, tmp = 1, 2, 0
        for i in range(3,n+1):
            tmp = first + second
            first = second
            second = tmp
        return tmp
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         use = {0:1, 1:1}
#         def cb(n, use):
#             if n in use.keys():
#                 return use[n]
#             else:
#                 rst = cb(n-1, use) + cb(n-2, use)
#                 use[n] = rst
#                 return use[n]
#         return cb(n, use)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         res = (((1+5**0.5)/2)**(n+1)-((1-5**0.5)/2)**(n+1))/((5)**0.5)
#         return int(res)


if __name__ == '__main__':
    t = Solution().climbStairs(995)

