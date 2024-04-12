# 1457. 二叉树中的伪回文路径

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root):
        ### solution 1: dfs 记录路径 + 判断伪回文（奇数数量个数）
        cnt = [0] * 10
        ans = 0
        
        def check_cnt(cur_cnt):
            odd_num = 0
            for each in cur_cnt[1:]:
                if (each%2):
                    odd_num += 1
                    if odd_num >= 2:
                        return
            nonlocal ans
            ans += 1
            return
            

        def dfs(x, cur_cnt):
            if x:
                if x.left:
                    cur_cnt[x.val] += 1
                    dfs(x.left, cur_cnt)
                    cur_cnt[x.val] -= 1
                
                if x.right:
                    cur_cnt[x.val] += 1
                    dfs(x.right, cur_cnt)
                    cur_cnt[x.val] -= 1

                if (not x.left) and (not x.right):
                    cur_cnt[x.val] += 1
                    check_cnt(cur_cnt)
                    cur_cnt[x.val] -= 1
                    
        dfs(root, cnt)
        return ans
