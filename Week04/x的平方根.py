# class Solution:
#     '''
#     求x的平方根。
#     x的平方根具有单调性、上下界、有序，所有可以采用二分法
#     '''
#     def mySqrt(self, x):
#         if x == 0:
#             return 0
#         left = 1           #左边界
#         right = x // 2 #右边界
#         while left < right:
#             mid = (left + right + 1) >> 1 #取右中位树
#             square = mid * mid
#             if square > x:#需要将右边界左移
#                 right = mid - 1
#             else:
#                 left = mid#需要将左边界右移
#         return left


class Solution:

    def mySqrt(self, x):
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)



if __name__ == '__main__':
    import time
    t1 = time.clock()
    t = Solution().mySqrt(9)
    print(t)
    print(time.clock()-t1)
