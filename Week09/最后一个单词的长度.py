class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([i for i in s.split(" ") if i !=""][-1])




if __name__ == "__main__":
    print(Solution().lengthOfLastWord("abc def hahah 123"))