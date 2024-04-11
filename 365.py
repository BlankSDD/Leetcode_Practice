# 365. 水壶问题

class Solution:
    def canMeasureWater(self, x, y, target):
        ### solution 1: dfs + flag 提前终止
        if target > x+y:
            return False
        if target in [0, x, y, x+y]:
            return True

        dp = [ [False]*(y+1) for _ in range(x+1) ]
        dp[0][0] = True

        vis = set()
        flag = False
        def dfs(i, j):
            if (i,j) in vis:
                return
            vis.add((i,j))

            if dp[i][j] == True:
                nonlocal flag
                if ((target == i+j) or (flag)):
                    flag = True
                    return

                # x 装满
                dp[x][j] = True
                dfs(x, j)

                # x 倒空
                dp[0][j] = True
                dfs(0, j)

                # y 装满
                dp[i][y] = True
                dfs(i, y)

                # y 倒空
                dp[i][0] = True
                dfs(i, 0)

                x_res = x-i
                y_res = y-j

                # x <- y 倒水
                if x_res >= j:
                    dp[i+j][0] = True
                    dfs(i+j, 0)
                else:
                    dp[x][j-x_res] = True
                    dfs(x, j-x_res)
                
                # x -> y 倒水
                if y_res >= i:
                    dp[0][i+j] = True
                    dfs(0, i+j)
                else:
                    dp[i-y_res][y] = True
                    dfs(i-y_res, y)
                
        dfs(0,0)
        
        # 判断是否可以达成 target
        # 方法 1: 加一个 flag， 在 dfs 遍历时就得到结果
        return True if flag else False
        
        # 方法 2: 遍历 dp[i][target-i] 即可，需注意超出边界
        # for i in range(target-y, x+1):
        #     if (dp[i][target-i]):
        #         return True
        #
        # 方法3: 方法 2 的优化
        # if any( [dp[i][target-i] for i in range(target-y, x+1) ] ):
        #     return True
        # return False


