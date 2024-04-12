# 2923. 找到冠军 I

class Solution:
    def findChampion(self, grid):
        
        ### solution 2: 贪心，遇见 0 就跳
        ###             或者  遇见 1 就跳
        n = len(grid)
        i = 0
        flag = False
        while not flag:
            flag = True
            for j in range(i+1, n):
                if grid[i][j] == 0:
                    i = j
                    flag = False
                    break
        return i


        ### solution 1: 判断每行是否都是 1 ，除了grid[i][i] 外
        ### 优化:
        ###      每行求和 / 每行计算 0或1 的个数
        ###      如果第 j 列的元素值都是 0，说明没有队伍可以击败 j 队
        

        # n = len(grid)
        # for i in range(n):
        #     if all(grid[i][:i]+grid[i][i+1:]):
        #         return i
        # return -1
