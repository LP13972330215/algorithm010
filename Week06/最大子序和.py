#!/usr/bin/python3
#Author:pliu

class Solution:
    '''
    题目：给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
    时间复杂度:O(n)、空间复杂度O(1)
    '''
    def maxSubArray(self, nums):
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i])
        return max(nums)


if __name__ == '__main__':
    # print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(int(1e9))

