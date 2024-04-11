# 1766. 互质树

from collections import defaultdict
import math
gcd_list = [set([1]) for i in range(51)]
gcd_list[0] = set()
gcd_list[1] = set([i for i in range(1, 51)])
for i in range(2, 50):
    for j in range(i+1, 51):
        if math.gcd(i,j) == 1:
            gcd_list[i].add(j)
            gcd_list[j].add(i)


class Solution:
    def getCoprimes(self, nums, edges):
        ### solution 2: dfs + 预处理 互质 的集合
        ###             nums[i] 的范围是 [1,50][1,50][1,50]
        n = len(nums)
        ans = [-1] * n
        c = defaultdict(list)
        for i,j in edges:
            c[i].append(j)
            c[j].append(i)
        
        # 记录每一个 节点ID 的深度（距离 根节点 0 的深度）
        dep = [-1] * n
        
        # 记录每一个    节点ID的值  （在[1,50]范围内） 
        # 出现在的      节点ID（越往右，深度越大）
        tmp = [ [] for _ in range(51) ]

        def dfs(x_ind, d):
            # x_ind, y_ind  节点x, y的ID
            # x, y          节点x, y的值
            x = nums[x_ind]
            dep[x_ind] = d
            
            # 遍历当前节点的值 x 的互质数 y
            # 找到 y 的最大深度，（因为是根据深度遍历，所以没有比当前更深的，更深的节点被 pop 出来了）
            # 更新 ans
            for y in gcd_list[x]:
                if not tmp[y]:
                    continue
                y_ind = tmp[y][-1]
                if (ans[x_ind] == -1) or (dep[y_ind] > dep[ans[x_ind]]):
                    ans[x_ind] = y_ind
            
            # 更新当前节点的值 x 出现的 节点ID 位置
            tmp[x].append(x_ind)

            # 根据树的边，从根节点往下遍历 尚未 遍历的节点
            # 深度 + 1
            for y_ind in c[x_ind]:
                if dep[y_ind] == -1:
                    dfs(y_ind, d+1)
            
            # 回溯，把当前节点，最深的 pop 出来
            tmp[x].pop()

        dfs(0, 1)
        return ans

        ### solution 1: 记录从 0 往下的连接，建立 父节点dict()
        ###             预处理 互质 的集合
        ###             nums[i] 的范围是 [1,50][1,50][1,50]
        ###             暴力遍历，超时
        # # math.gcd(x, y)
        # n = len(nums)
        # ans = [-1] * (n)

        # p = [-1] * (n)
        # c = defaultdict(list)
        # for i,j in edges:
        #     c[i].append(j)
        #     c[j].append(i)

        # tmp = [0]
        # searched = set([0])
        # while tmp:
        #     cur = tmp.pop(0)
        #     for nxt in c[cur]:
        #         if nxt in searched:
        #             continue
        #         tmp.append(nxt)
        #         searched.add(nxt)
        #         p[nxt] = cur

        # for i in range(1, n):
        #     j = p[i]
        #     while j >= 0:
        #         if (nums[j] in gcd_list[nums[i]]):
        #             break
        #         j = p[j]
        #     ans[i] = j
                
        # return ans

        
