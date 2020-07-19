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


if __name__ == '__main__': # 70 +60 +30 +60 +60
    # t = Solution().mySqrt(9)
    a = '65535'
    # import sys
    # @property
    # print(sys.getsizeof(a))
    # load_csv()
    # check_filed()
    # map_pri()
    # combination_syslog()
    # send_syslog()
    # import logging
    # import logging.handlers  # handlers要单独import
    # import socket
    # logger = logging.getLogger()
    # fh = logging.handlers.SysLogHandler(('10.10.50.203', 514), logging.handlers.SysLogHandler.LOG_AUTH)
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # fh.setFormatter(formatter)
    #
    # logger.addHandler(fh)
    # logger.warning("<34>Oct 11 22:14:15 mymachine su[1111]: root failed for lonvick on /dev/pts/8")
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto("<34>Oct 11 22:14:15 mymachine su[1111]: root failed".encode(),('10.10.50.111',514))
    s.close()


