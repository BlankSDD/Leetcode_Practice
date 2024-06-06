# 3067. 在带权树网络中统计可连接服务器对数目

from collections import defaultdict
from typing import List


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        ### solution 1: dict建图
        ###             遍历可能作为 中间服务器 c 的节点
        ###             把 c 作为根节点 root， 遍历其子树 c1, c2, c3, ...
        ###             任意可整除 signalSpeed 的不同子树中的节点可以把 c 当作中间服务器
        ###             例：      c
        ###                 c1  c2  c3  c4
        ###                 c1 中整除 signalSpeed 的节点， 与 ，
        ###                 c2 中整除 signalSpeed 的节点
        ###                 可以把 c 当作中间服务器
        ###             所以：
        ###             遍历其子树 c1, c2, c3, ..., 分别计数子树中包含可以整除 signalSpeed 的节点数量
        ###             遍历包含的数量， c1 * (其他子树包含节点数量) + c2 * (其他子树包含节点数量) +  c3 * (其他子树包含节点数量) + ...

        # dict 建图
        conn = defaultdict(list)
        for i,j,w in edges:
            conn[i].append([j, w])
            conn[j].append([i, w])
        
        # dfs 搜索 c1 中可以整除 signalSpeed 的节点数量
        # 需要加上上一次的 权重 d
        def dfs(root, d):
            nonlocal searched
            if searched[root]:
                return 0
            
            searched[root] = True
            res = 0
            if (d % signalSpeed == 0):
                res += 1

            for i,w in conn[root]:
                # 随深度加深， 加上上一次的 权重 d
                res += dfs(i, d+w)
            
            return res

        # 最大节点编号 n ， 总共有 n+1 个节点
        n = max(conn.keys())
        ans = [0] * (n+1)

        # 遍历所有节点
        for c in range(n+1):
            # 只有一个边的节点，不可能作为 中间服务器
            if (not c in conn) or (len(conn[c]) <= 1):
                continue
            
            children_number = len(conn[c])
            children_satisfied_signalSpeed = []

            # 记录已经遍历过的子树节点
            searched = [False] * (n+1)
            searched[c] = True
            # 遍历 中间服务器 c 的子树
            for child, w in conn[c]:
                # 对每个子树 作 dfs 遍历
                css = dfs(child, w)
                children_satisfied_signalSpeed.append(css)

            c_res = 0
            total_css = sum(children_satisfied_signalSpeed)
            # 遍历包含的数量， c1 * (其他子树包含节点数量)
            # 其他子树包含节点数量 = 总 - c1
            for css in children_satisfied_signalSpeed:
                c_res += css * (total_css - css)
            # c1 * (c2 + c3) + c2 * (c1 + c3) + c3 * (c1 + c2)
            # 重复计算了一遍，需要 // 2
            ans[c] = c_res//2
        
        return ans
