# LCR 194. 二叉树的最近公共祖先

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ### solution 3: dfs遍历递归

        # 只要搜到p 或 q,即返回
        if root in (None, p, q):
            return root
        # 向下搜索
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # p q都搜到就返回当前节点
        if left and right:
            return root
        return left or right
        
        
        ### solution 2: dfs遍历递归
        #               在根两边，沿着搜索路径向上是否已经找到p q
        #               只有根/其中一个为根，返回根节点
        # ans = root
        # def dfs(x, y, z):
        #     if (not x): return False
        #     l = dfs(x.left, y, z)
        #     r = dfs(x.right, y, z)
        #     # (两边都找到) or   (根为p或q and 找到其中一个)
        #     if (l and r) or (((x.val == y.val) or (x.val == z.val)) and (l or r)):
        #         ans = x
        #     return l or r or (x.val == y.val) or (x.val == z.val)
        
        # dfs(root, p, q)
        # return ans
        




        ### solution 1: dfs + dict记录parents , 在便其中一个所有的父节点
        # tmp = [root]
        # parents = dict()
        # find_p = False
        # find_q = False

        # while tmp and ((not find_p) or (not find_q)):
        #     cur = tmp.pop()
        #     if cur == p:
        #         find_p = True
        #     if cur == q:
        #         find_q = True
        #     if cur.left:
        #         tmp.append(cur.left)
        #         parents[cur.left] = cur
        #     if cur.right:
        #         tmp.append(cur.right)
        #         parents[cur.right] = cur
        
        # p_parent = set([p])

        # while p != root:
        #     p = parents[p]
        #     p_parent.add(p)
        # while not q in p_parent:
        #     q = parents[q]
        
        # return q
            
        
