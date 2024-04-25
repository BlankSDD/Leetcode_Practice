# 2385. 感染二叉树需要的总时间


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ### solution 3: dfs一次遍历，判断是否找到 start， 同时记录深度，以root为中间点

        ans = 0

        # 该 dfs 返回 深度+bool （是否搜到start这一侧的树）
        def dfs(x):
            nonlocal ans
            if not x:
                return (0, False)
            
            l_d, l_found = dfs(x.left)
            r_d, r_found = dfs(x.right)

            # 当前节点为 start
            if (x.val == start):
                ans = max(l_d, r_d)
                return (1, True)
            
            # 左右有一侧搜到 start
            if (l_found or r_found):
                ans = max(ans, l_d+r_d)

                if l_found:
                    return (l_d+1, True)
                else:
                    return (r_d+1, True)
            
            # 左右两侧均未搜到 start
            return (max(l_d, r_d)+1, False)
        
        dfs(root)
        return ans
            
        
        ### solution 2: dfs建图 + 队列bfs搜图
        # conn = defaultdict(list)
        # def dfs(x):
        #     if x:
        #         if x.left:
        #             conn[x.left.val].append(x.val)
        #             conn[x.val].append(x.left.val)
        #             dfs(x.left)
        #         if x.right:
        #             conn[x.right.val].append(x.val)
        #             conn[x.val].append(x.right.val)
        #             dfs(x.right)

        # dfs(root)

        # searched = set([start])       
        # d = -1

        # cur_tmp = [start]
        # while cur_tmp:
        #     d += 1

        #     nxt_tmp = []
            
        #     for cur in cur_tmp:
        #         for nxt in conn[cur]:
        #             if not (nxt in searched):
        #                 searched.add(nxt)
        #                 nxt_tmp.append(nxt)
            
        #     cur_tmp = nxt_tmp

        # return d
        
        ### solution 1: dfs建图 + dfs搜图
        # conn = defaultdict(list)
        # def dfs(x):
        #     if x:
        #         if x.left:
        #             conn[x.left.val].append(x.val)
        #             conn[x.val].append(x.left.val)
        #             dfs(x.left)
        #         if x.right:
        #             conn[x.right.val].append(x.val)
        #             conn[x.val].append(x.right.val)
        #             dfs(x.right)

        # searched = set([start])
        # max_d = 0
        # def dfs_cal_d(x, d):
        #     nonlocal max_d
        #     max_d = max(max_d, d)
        #     for y in conn[x]:
        #         if not (y in searched):
        #             searched.add(y)
        #             dfs_cal_d(y, d+1)

        # dfs(root)
        # dfs_cal_d(start, 0)

        # return max_d
