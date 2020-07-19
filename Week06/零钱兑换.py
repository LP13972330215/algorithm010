# #!/usr/bin/python3
# #Author:pliu

class Solution:
    def coinChange(self, coins, amount):

        dp = [float("inf")] * (amount + 1)
        print(dp)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if (i >= coin):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if (dp[-1] != float("inf")) else -1



if __name__ == '__main__':
    print(Solution().coinChange([1,2,5],11))



