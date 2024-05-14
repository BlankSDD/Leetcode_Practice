# LCR 053. 二叉搜索树中的中序后继

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        ### solution 2: 根据二叉搜索树rule（严格大小排序）进行搜索
        # 如果 p 有右子树
        tmp = p.right
        if tmp:
            while tmp.left:
                tmp = tmp.left
            return tmp

        # 如果 p 没有右子树， 找到比 p 大的最小的 节点即可
        cur = root
        ans = None
        while cur:
            if (cur.val > p.val):
                ans = cur
                cur = cur.left
            else:
                cur = cur.right

        return ans

        ### solution 1: DFS + 根据二叉搜索树rule（严格大小排序）进行搜索
        # # 如果 p 有右子树
        # tmp = p.right
        # if tmp:
        #     while tmp.left:
        #         tmp = tmp.left
        #     return tmp

        # # 如果 p 没有右子树， DFS找到比 p 大的最小的 节点即可
        # def dfs(x):
        #     if (not x):
        #         return None
            
        #     if (x.val > p.val):
        #         l_x = dfs(x.left)
        #         if l_x:
        #             return l_x
        #         else:
        #             return x
        #     else:
        #         r_x = dfs(x.right)
        #         return r_x
            
        # ans = dfs(root)
        # return ans
                
        
