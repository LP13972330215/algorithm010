#!/usr/bin/python3
#Author:pliu

# class Solution:
#     def findCircleNum(self, M):
#         p = [i for i in range(len(M))]
#         def find(x):
#             if p[x] != x:
#                 p[x] = find(p[x])
#             return p[x]
#
#         for i in range(len(M)):
#             for j in range(len(M)):
#                 if M[i][j] == 1:
#                     a = find(i)     ## 这里就是merge操作，重新写一个函数太麻烦了
#                     b = find(j)
#                     p[a] = b       ## 直接修改数组中的根节点
#
#         for i in range(len(M)):   ## 需要多这一步，将所有的点都回归其根节点，然后在判断根的数量有多少
#             find(i)
#         return len(set(p))
# class Solution:
#     def findCircleNum(self, M):
#         N = len(M)
#         count = 0
#         visited = set()
#
#         def dfs(i):
#             for j in range(N):
#                 if M[i][j] and j not in visited:
#                     visited.add(j)
#                     dfs(j)
#
#         for i in range(N):
#             if i not in visited:
#                 count += 1
#                 visited.add(i)
#                 dfs(i)
#
#         return count
class Solution:
    def findCircleNum(self, M):
        f = {}
        s = {}
        count = len(M)

        def find(x):
            f.setdefault(x, x)
            # 路径压缩
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            nonlocal count
            x_father, y_father = find(x), find(y)
            if x_father == y_father: return
            # 将小树的根节点连接到大叔的根节点
            if s.setdefault(x_father, 1) < s.setdefault(y_father, 1):
                f[x_father] = y_father
                s[y_father] += s[x_father]
            else:
                f[y_father] = x_father
                s[x_father] += s[y_father]
            count -= 1

        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    union(i, j)
        return count


if __name__ == '__main__':
    M= [[1,1,0],[1,1,0],[0,0,1]]
    print(Solution().findCircleNum(M))