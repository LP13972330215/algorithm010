#！/usr/bin/python3
#Author:pliu
if __name__ == '__main__':
    class Solution:
        def search(self, nums, target):
            # 确定查找的上下界
            low, high = 0, len(nums) - 1
            while low <= high:  # 当low == high时还剩下最后一个值需要进行检验
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1  # +1是因为mid已经验证过不符合条件，新的区间又mid+1开始
                elif nums[mid] > target:
                    high = mid - 1  # 这里+1同上面原因相同
                else:
                    return mid
            return -1
    t=Solution().search([2,11,15,19,30,32,61,72,88,90,96],15)