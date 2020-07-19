#!/usr/bin/python3
#Author:pliu


class Solution:
    def minimumTotal(self, triangle):
        '''
        思路：从倒数第二行开始往上覆盖，dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        :param triangle:
        :return:
        '''
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r + 1][c:c + 2])
        return triangle[0][0]


if __name__ == '__main__':
    data = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(Solution().minimumTotal(data))
