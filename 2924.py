# 2924. 找到冠军 II

class Solution:
    def findChampion(self, n, edges):
        ans = [True] * n
        for i,j in edges:
            ans[j] = False

        ### 遍历判断冠军
        res = -1
        for i,cur in enumerate(ans):
            if cur:
                if res != -1:
                    return -1
                res = i
        return res

        ### 计数判断冠军
        # if ans.count(True) == 1:
        #     return ans.index(True)
        # else:
        #     return -1
