class Solution:
    def longestCommonPrefix(self, strs):
        """
        time complexity:O(mn)
        :param strs:
        :return:
        """
        # if not strs:
        #     return ""
        # length, count = len(strs[0]), len(strs)
        # for i in range(length):
        #     c = strs[0][i]
        #     if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
        #         return strs[0][:i]
        # return strs[0]

        ans = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans

if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))


