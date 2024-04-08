# 2192. 有向无环图中一个节点的所有祖先
class Solution:
    def getAncestors(self, n, edges):
        ### solution 2: dfs + 2个graph(防重复搜索)
        p = [[] for _ in range(n)]
        ans = [[] for _ in range(n)]

        for f,t in edges:
            p[t].append(f)
        
        def dfs(cur, nxt, vis):
            for j in p[nxt]:
                if not vis[j]:
                    vis[j] = True
                    ans[cur].append(j)
                    dfs(cur, j, vis)
        
        for i in range(n):
            dfs(i, i, [False] * n)
            ans[i].sort()
        return ans



        ### solution 1: 暴力遍历每一个node + 搜索
        # ans = [[] for _ in range(n)]

        # for f,t in edges:
        #     ans[t].append(f)
        
        # for i in range(n):
        #     tmp = ans[i]
        #     searched = set(tmp)
        #     while tmp:
        #         cur = tmp.pop()
        #         for j in ans[cur]:
        #             if not j in searched:
        #                 tmp.append(j)
        #                 searched.add(j)
        #     ans[i] = sorted(list(searched))
        
        # return ans
        
