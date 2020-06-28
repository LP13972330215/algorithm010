class Solution:
    '''
    给定两个整数n、k，返回1...n中所有出现的k个数的组合
    '''
    def combine(self, n, k):
        res = []
        def backtrack(i, k, tmp):
            if k == 0:
                res.append(tmp)
                return
            for j in range(i, n + 1):
                backtrack(j+1, k-1, tmp + [j])
        backtrack(1, k, [])
        return res

if __name__ == '__main__':
    print(Solution().combine(4,2))

