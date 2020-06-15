class Solution(object):
    def twoSum(self, nums, target=None):
        """
        TODO：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。
        你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #暴力破解，时间复杂度O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i,j

        #哈希表,时间复杂度O(n)
        hashmap = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [hashmap.get(diff), i]
            hashmap[value] = i

