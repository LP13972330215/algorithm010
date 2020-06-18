class Solution:
        #时间复杂度:O(n^2),空间复杂度:O(1)
        def threeSum(self, nums):
            if not nums:
                return []
            # 正式处理之前，先将数组排序
            nums = sorted(nums) #时间复杂度:O(nlogn)
            n = len(nums)
            res = []
            # 假设数组为[0,1,2,3,4,5,6,7,8,9,10]
            # 第三个指针k最多到下标8位置，因为后面两个位置需要留给另外两个指针
            for k in range(n-2):
                # nums[k]>0，说明后面的元素肯定也大于0，最后结果肯定>0，故直接跳出
                if nums[k]>0:
                    break
                # 如果当前元素和前面一个元素一样，忽略重复元素
                if k>0 and nums[k-1]==nums[k]:
                    continue
                # 定义另外两个指针 i 和 j
                i,j = k+1,n-1
                while i<j:
                    tmp = nums[i]+nums[j]+nums[k]
                    # 如果三数之和>0，说明最右边的值太大了，
                    if tmp>0:
                        j -= 1
                        while i<j and nums[j+1]==nums[j]:
                            j -= 1
                    # 如果三数之和<0，说明左边的值太小了
                    elif tmp<0:
                        i += 1
                        while i<j and nums[i-1]==nums[i]:
                            i += 1
                    # 三数之和等于0，保存结果
                    # 同时左指针往右移动，右指针往左移动，
                    # 如果移动过程中碰到重复元素，则继续移动
                    else:
                        res.append([ nums[k],nums[i],nums[j] ])
                        i += 1
                        j -= 1
                        while i<j and nums[i-1]==nums[i]:
                            i += 1
                        while i<j and nums[j+1]==nums[j]:
                            j -= 1
            return res
