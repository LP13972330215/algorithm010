class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, dic = set(), {}
        num_len = len(nums)
        nums.sort()
        for i in range(num_len):
            for j in range(i+1, num_len):
                key = nums[i] + nums[j]
                if key not in dic:
                    dic[key] = [(i, j)]
                else:
                    dic[key].append((i, j))
        for i in range(num_len):
            for j in range(i+1, num_len-2):
                exp = target - nums[i] - nums[j]
                if exp in dic:
                    for tmpIndex in dic[exp]:
                        if tmpIndex[0] > j:
                            res.add((nums[i], nums[j], nums[tmpIndex[0]], nums[tmpIndex[1]]))
        # return [list(i) for i in res]
        return res

if __name__== '__main__':
    data = [1, 0, -1, 0, -2, 2]
    t=Solution().fourSum(data, 0)
    print(t)
