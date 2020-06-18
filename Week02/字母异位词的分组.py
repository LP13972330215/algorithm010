class Solution:
    '''
    字母异位词的分组，将数组中的异位词进行分类
    '''
    def groupAnagrams(self, strs):
        #时间复杂度：O(n)
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())

test_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(test_data))
