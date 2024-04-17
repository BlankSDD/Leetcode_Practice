# 924. 尽量减少恶意软件的传播

### 与 928 不同
### 924： 删除节点 -> 仅让该节点变为正常，不删除其相关的边
### 928： 删除节点 -> 删除该节点，同时删除其相关的边

from collections import defaultdict
from math import inf
from typing import List

class UnionSet:
    def __init__(self, n):
        self.p = { i:i for i in range(n) }
        self.rank = { i:1 for i in range(n) }

    def find_root(self, x):
        root = x
        while root != self.p[root]:
            root = self.p[root]
        
        self.p[x] = root
        return root
    
    def union_set(self, x, y):
        x_root = self.find_root(x)
        y_root = self.find_root(y)
        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.p[x_root] = y_root
                self.rank[y_root] += self.rank[x_root]
            else:
                self.p[y_root] = x_root
                self.rank[x_root] += self.rank[y_root]

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        us = UnionSet(n)
        
        # 建立有 initial 的并查集
        for i in range(n-1):
            for j in range(i+1, n):
                if graph[i][j]:
                    us.union_set(i, j)

        # 计算每个 root 被哪些 initial 感染了
        tmp = defaultdict(list)
        
        for cur in initial:
            rt = us.find_root(cur)
            rk = us.rank[rt]
            tmp[(rt, rk)].append(cur)
        
        # 遍历被感染的 root， 记录 最大感染数 和 最小 root 值
        max_infect = -1
        min_cur = inf
        for k,v in tmp.items():
            if len(v) > 1:
                continue
            
            if (max_infect < k[1]) or ((max_infect == k[1]) and (min_cur > v[0])):
                max_infect = k[1]
                min_cur = v[0]
        
        if min_cur < inf:
            return min_cur
        else:
            return min(initial)
