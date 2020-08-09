#！/usr/bin/python3
#Author:pliu


# Dynamic programming.
class Solution:
    def lengthOfLIS(self, nums):
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    print(i,j)
                    print(nums[i],nums[j])
                    dp[i] = max(dp[i], dp[j] + 1)
                    print(dp)
        return max(dp)



if __name__ == "__main__":
    data = [11,1,2,3,22,333,1112]
    print(Solution().lengthOfLIS(data))
    from multiprocessing import managers

