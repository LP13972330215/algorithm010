class Solution(object):
    '''
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
    字母异位词解释：两个字符串，长度相同，并且每个字母出现的次数也相同。
    方法有两种：1、先排序，然后对比两个字符串是否相等。时间复杂度:O(nlogn)
              2、计算字符串中的每个字母出现的次数(哈希表示法)。时间复杂度O(n)
              3、对比字符串中所有字母对应的十进制数的总和
    '''

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True


