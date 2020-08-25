#！/usr/bin/python3
#Author:pliu

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 2], cost[i - 1]) + cost[i]
        return min(cost[-2], cost[-1])


if __name__ == "__main__":
    print(Solution().minCostClimbingStairs([10,15,20]))