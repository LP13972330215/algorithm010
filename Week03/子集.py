# class Solution:
#     '''
#     迭代
#     时间复杂度:O(Nx2^N)、空间复杂度O(Nx2^N)
#     '''
#     def subsets(self, nums):
#         output = [[]]
#         for num in nums:
#             output += [curr + [num] for curr in output]
#         return output
class Solution:
    '''
    时间复杂度:O(n!),空间复杂度:O(1)
    '''
    def subsets(self, nums):
        res=[]
        n=len(nums)
        def track_back(i,tmp):
            if(i==n):
                return
            res.append(tmp)
            for j in range(i+1,n):
                track_back(j,tmp+[nums[j]])
        track_back(-1,[])
        return res


t = Solution().subsets([1,2,3])
print(t)



