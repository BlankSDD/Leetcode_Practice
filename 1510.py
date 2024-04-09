# 1510. 石子游戏 IV
class Solution:
    def winnerSquareGame(self, n):
        m = int(pow(n, 1/2))
        dp = [False]*(n+1)
        
        ### f[0]=false，即没有石子时，先手会输掉游戏
        ### 所以不用判断 整平方数
        # for i in range(1, m+1):
        #     dp[i*i] = True
        
        for i in range(n+1):
            for j in range(1, int(pow(i, 1/2))+1 ):
                ### f[0]=false，即没有石子时，先手会输掉游戏
                ### 所以不用判断 整平方数
                # if dp[i]:
                #     break
                
                ### 任何一个 f[i−k*k] 为必败态时，f[i]即为必胜态
                if not dp[i-j*j]:
                    dp[i] = True
                    break
        
        return dp[n]
