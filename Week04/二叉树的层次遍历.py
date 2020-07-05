from collections import  deque


class TreeNode:
    def __init__(self, value,left=None,right=None):
        self.val = value
        self.left = left
        self.right = right


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res


if __name__ == '__main__':
    nodeTree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                            right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))
    print(Solution().levelOrder(nodeTree))


