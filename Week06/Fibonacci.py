#!/usr/bin/python3
#Author:pliu

# class Solution:
#     import functools
#     @functools.lru_cache(None)
#     def fib(self, n):
#         if n<2:
#             return n
#         return (self.fib(n-1)+self.fib(n-2))


class Solution:
    '''采用递归加记忆搜索法。时间复杂度:O(n),但另外需消耗O(n)的额外空间'''
    def fib(self, n):
        self.hashmap = {}
        self.hashmap[0]=0
        self.hashmap[1]=1
        def helper(n):
            if n<2:
                return n
            if n in self.hashmap:
                return self.hashmap[n]
            else:
                result = helper(n-1)+helper(n-2)
                self.hashmap[n]=result
                return result
        return helper(n)

class Solution:
    '''采用动态规划。时间复杂度:O(n)'''
    def fib(self, n):
        num = dict()
        num[0] = 0
        num[1] = 1
        if n > 1:
            for i in range(2,n+1):
                num[i] = num[i-2] + num[i-1]
        return num[n]


if __name__ == '__main__':
    t = Solution().fib(30)
    print(t)