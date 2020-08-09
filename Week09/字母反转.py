

class Solution:
    def reverseOnlyLetters(self, S):
        """
        双指针逼。时间复杂度:O(n),空间复杂度O(n)
        :param S:
        :return:
        """
        l1=0;l2=len(S)-1
        S=list(S)
        while(l2 > l1):
            if S[l2].isalpha() and S[l1].isalpha():
                S[l2],S[l1]=S[l1],S[l2]
                l1+=1
                l2-=1
            elif not S[l2].isalpha():
                l2-=1
            elif not S[l1].isalpha():
                l1+=1
        return ''.join(S)

if __name__ == "__main__":
    a = "ab-cd"
    print(Solution().reverseOnlyLetters(a))