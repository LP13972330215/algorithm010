#!/usr/bin/python3
#Author:pliu

class Solution:
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]#临界边
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]#临界边
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == '__main__':
    data = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    print(Solution().minPathSum(data))