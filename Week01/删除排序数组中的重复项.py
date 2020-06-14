class Solution(object):
    def removeDuplicates(self, nums):
        """
        TODO:数组[1,1,1,2,2,2,2,3],将其连续重复的元素删除，只保留一个。
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        n = 0
        for i in range(1, len(nums)):
            if nums[n] != nums[i]:
                n += 1
                nums[n] = nums[i]
        return n + 1




