class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')','[':']','{':'}'}
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif i == dic[stack.pop()]:
                    pass
                else:
                    return False
        return len(stack) == 0

a = ['{',']','[',']','}']
print(Solution().isValid(a))


