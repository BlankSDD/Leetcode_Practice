# 928. 尽量减少恶意软件的传播 II

### 与 924 不同
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
    
    def conn(self, x, y):
        return self.find_root(x) == self.find_root(y)

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        ini_set = set(initial)
        us = UnionSet(n)

        # 建立无 initial 的并查集
        for i in range(n-1):
            for j in range(i+1, n):
                if (not graph[i][j]) or (i in ini_set) or (j in ini_set):
                    continue
                else:
                    us.union_set(i, j)
        
        # 计算每个 initial 加入时，会感染的 root
        initial_infected_root = defaultdict(set)
        # 并计算每个 root 被感染的次数，一个 initial 只能感染一个 root 一次，同一个 initial 重复感染同一个 root 不算
        root_infected_times = defaultdict(int)

        for i in initial:
            i_infected_root = set()
            for j,f in enumerate(graph[i]):
                if (not f) or (j in ini_set):
                    continue
                
                j_root = us.find_root(j)
                i_infected_root.add(j_root)
            
            initial_infected_root[i] = i_infected_root

            for j_root in i_infected_root:
                root_infected_times[j_root] += 1
        
        # 对每一个 initial 计算有效感染数量 （即 root 仅被所有 initial 感染这一次的）
        # 同时更新最后结果，记录结果需要的 initial 的值 和 感染次数
        ans = inf
        max_infect = -1

        for i,i_infected_root in initial_infected_root.items():
            i_infect_num = 0
            for r in i_infected_root:
                if root_infected_times[r] == 1:
                    i_infect_num += us.rank[r]
                 
            if (max_infect < i_infect_num) or ((max_infect == i_infect_num) and (i < ans)):
                ans = i
                max_infect = i_infect_num
        
        return ans





