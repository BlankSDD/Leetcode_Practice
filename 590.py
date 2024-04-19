# 590. N 叉树的后序遍历

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


class Solution:
    def postorder(self, root) -> List[int]:
        ### solution 2: 重新定义一个 dfs

        ans = []
        def dfs(x):
            if not x:
                return
            
            for c in x.children:
                dfs(c)
                
            ans.append(x.val)
        
        dfs(root)
        return ans

        ### solution 1: 递归
        # ans = []
        # if not root:
        #     return
        
        # for each in root.children:
        #     ans += self.postorder(each)
        
        # ans.append(root.val)
        # return ans

        
