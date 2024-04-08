# 1026. 节点与其祖先之间的最大差值

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root):
        ### solution 3: 记录路径
        # p = defaultdict(list)
        # def dfs(x):
        #     if x: 
        #         if x.left:
        #             p[x.left] += p[x]
        #             p[x.left].append(x)
        #             dfs(x.left)
        #         if x.right:
        #             p[x.right] += p[x]
        #             p[x.right].append(x)
        #             dfs(x.right)
        # dfs(root)

        # ans = 0
        # for k,v in p.items():
        #     for i in v:
        #         ans = max(ans, abs(k.val - i.val))
        # return ans
        
        ### solution 2: dfs + 传递子树的最小/大值 + 优化
        ans = 0

        def dfs(x, sub_min, sub_max):
            if not x:
                return 0
            
            ans = max([abs(x.val-sub_min), abs(x.val-sub_max)])
            sub_min = min(sub_min, x.val)
            sub_max = max(sub_max, x.val)
            
            ans = max(ans, dfs(x.left, sub_min, sub_max))
            ans = max(ans, dfs(x.right, sub_min, sub_max))
            return ans
        
        return dfs(root, root.val, root.val)

        ### solution 1: dfs + 传递子树的最小/大值
        # ans = -inf

        # def dfs(x, sub_min, sub_max):
        #     if not x:
        #         return [sub_min,sub_max]
            
        #     sub_min = min(sub_min, x.val)
        #     sub_max = max(sub_max, x.val)
        #     if x.left:
        #         i,j = dfs(x.left, x.val, x.val)
        #         sub_min = min(sub_min, i)
        #         sub_max = max(sub_max, j)
        #     if x.right:
        #         i,j = dfs(x.right, x.val, x.val)
        #         sub_min = min(sub_min, i)
        #         sub_max = max(sub_max, j)
            
        #     nonlocal ans
        #     ans = max([ans, abs(x.val-sub_min), abs(x.val-sub_max)])

        #     return [sub_min,sub_max]
        
        # dfs(root, inf, -inf)
        # return ans
        
