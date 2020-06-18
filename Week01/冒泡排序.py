
def bubble_sort(nums):
    '''
    冒泡排序,时间复杂度O(n^2),空间复杂度O(1)
    '''
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 2):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums




