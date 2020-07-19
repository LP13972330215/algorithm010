#!/usr/bin/python3
#Author:pliu

class Solution:
    '''动态规划。时间复杂度:O(n*m)、空间复杂度O(n)'''
    def uniquePaths(self, m, n):
        #m、n必须大于2且为正整数
        cur = [1] * n #将两维压缩成一维
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]


if __name__ == '__main__':
    Solution().uniquePaths(6,5)



