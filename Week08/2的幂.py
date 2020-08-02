#！/usr/bin/python3
#Author:pliu

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return n & (n - 1) == 0


if __name__ == "__main__":
    # print(Solution().isPowerOfTwo(218))
    import time

    from functools import lru_cache


    @lru_cache(maxsize=512)
    def fib(number: int) -> int:
        if number == 0: return 0
        if number == 1: return 1
        return fib(number - 1) + fib(number - 2)


    start = time.time()
    fib(40)
    print(f'Duration: {time.time() - start}s')