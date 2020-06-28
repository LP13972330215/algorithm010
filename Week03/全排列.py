class Solution:
    '''
    给定一个没有重复数字的序列，返回其所有的全排列
    '''
    def permute(self, nums):
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

if __name__ == '__main__':
    data = [1,2,3]
    t = Solution().permute(data)
    print(t)