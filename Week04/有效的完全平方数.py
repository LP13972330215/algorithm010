class Solution:
    '''
    判断一个数是否为有效完全平方数
    '''

    def isPerfectSquare(self, num):
        if num==1:return True
        a = 1
        b = num
        while a <= b:
            mid = (a + b) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                b = mid - 1
            else:
                a = mid + 1
        return False

if __name__ == '__main__':
    t = Solution().isPerfectSquare(-8)
    print(t)

