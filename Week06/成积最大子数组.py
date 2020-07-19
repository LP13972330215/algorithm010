#!/usr/bin/python3
#Author:pliu


class Solution:
    '''
    给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
    '''
    def maxProduct(self, nums):
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums+reverse_nums)


if __name__ =='__main__':
    nums= [2,3,-2,4,0,2,4,11,22,33,0,-11]
    print(Solution().maxProduct(nums))

