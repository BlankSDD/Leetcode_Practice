# 1379. 找出克隆二叉树中的相同节点

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        ### solution 2: 递归遍历, None or Any = Any
        if original == None or original == target:
            return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)

        ### solution 1: 树的遍历
        # tmp = [cloned]
        # y = target.val

        # while tmp:
        #     cur = tmp.pop()
        #     if cur.val == y:
        #         return cur
        #     if cur.left:
        #         tmp.append(cur.left)
        #     if cur.right:
        #         tmp.append(cur.right)

        # return cur
        
