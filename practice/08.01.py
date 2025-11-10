# 面试题 08.01. 三步问题

MOD = pow(10, 9) + 7
dp = [0, 1, 2, 4]
for i in range(4, 1000001):
    dp.append((dp[-1]+dp[-2]+dp[-3])%MOD)
    

class Solution:
    def waysToStep(self, n: int) -> int:
        ### solution 2: dp + 提前遍历 + 存储
        return dp[n]

        
        ### solution 1: 递归，超时了
        # MOD = pow(10, 9) + 7
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # elif n == 3:
        #     return 4
        # else:
        #     return (self.waysToStep(n-1) + self.waysToStep(n-2) + self.waysToStep(n-3))%MOD
