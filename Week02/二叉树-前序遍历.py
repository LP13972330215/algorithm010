
class NodeTree:
    def __init__(self, val=None, right=None, left=None):
        """创建二叉树
        Argument:
            left: BinTree
                左子树
            right: BinTree
                右子树
        Return:
            Tree
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    递归
    '''
    def recursion(self, root):
        res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return res

    def inorderTraversal(self, root):
        stack,rst = [root],[]
        while stack:
            i = stack.pop()
            if isinstance(i,NodeTree):
                # stack.extend([i.right,i.val,i.left]) ## 中序遍历
                # stack.extend([i.val,i.right,i.left]) ## 后序遍历
                stack.extend([i.right,i.left,i.val]) ## 前序遍历
            elif isinstance(i,int):
                rst.append(i)
        return rst

    def levelOrder(self, root):
        queue, res = [root], []
        print(queue)
        while queue:
            i = queue.pop(0)
            if isinstance(i, NodeTree):
                queue.extend([i.val, i.left, i.right])
            elif isinstance(i, int):
                res.append(i)
        return res
    def preorder(self,root):
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                return
            res.append(root.val) #先将根结点加入到结果
            dfs(root.left)#左
            dfs(root.right)#右
        dfs(root)
        return res
    def inorder(self,root):
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                return
            dfs(root.left)  # 左
            res.append(root.val) #先将根结点加入到结果
            dfs(root.right)#右
        dfs(root)
        return res
    def postorder(self,root):
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                return
            dfs(root.left)  # 左
            dfs(root.right)#右
            res.append(root.val) #先将根结点加入到结果
        dfs(root)
        return res



nodeTree = NodeTree(1, left=NodeTree(2,left=NodeTree(4,right=NodeTree(7))),
                        right=NodeTree(3,left=NodeTree(5),right=NodeTree(6)))
print(Solution().levelOrder(nodeTree))
