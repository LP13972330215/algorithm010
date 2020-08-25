class Solution(object):
    def reverse(self, x: int) -> int:
        if -2**31 <=x <=2**31 -1:
            a = str(x).replace('-','')
            a=int(a[::-1])
            if a< 2**31:
                if x >=0:
                    return a
                else:
                    return -a
            else:return 0
        else:return -1


if __name__ == "__main__":
    a = -123
    print(Solution().reverse(a))
