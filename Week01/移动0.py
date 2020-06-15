class Solution(object):
    def moveZeroes(self, nums):
        """
        TODO：将列表中为0的元素移动到末尾，并保持非0元素的相对位置
        要求：不能使用额外的数组，尽量少操作
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
a = [1,0,2,0,3]
Solution().moveZeroes(a)
#上述方法的时间复杂度为O(n)、空间复杂度O(1)