class Solution(object):
    def search(self, nums, target):
        """
        搜索旋转排序数组
        """
        left, right = 0,len(nums)-1
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    t = Solution().search([4,5,6,7,0,1,2],1)
    print(t)
