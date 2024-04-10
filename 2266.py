# 2266. 统计打字方案数

mod = 10**9 + 7
three = '234568'
four = '79'
three_DP = [0, 1, 2, 4]
four_DP = [0, 1, 2, 4, 8]
def countDP(c, n):
    if not c in four:
        cur = len(three_DP)
        while cur <= n:
            three_DP.append((three_DP[cur-1] + three_DP[cur-2] + three_DP[cur-3])%mod)
            cur += 1
        return three_DP[n]
    else:
        cur = len(four_DP)
        while cur <= n:
            four_DP.append((four_DP[cur-1] + four_DP[cur-2] + four_DP[cur-3] + four_DP[cur-4])%mod)
            cur += 1
        return four_DP[n]
    
class Solution:
    
    def countTexts(self, pressedKeys):
        ### soltuion 1: dp + 全局存储
        ### f[i]=f[i−1]+f[i−2]+f[i−3]
        ### g[i]=g[i−1]+g[i−2]+g[i−3]+g[i−4]
        n = len(pressedKeys)
        ans = 1

        cnt = 1

        # 遍历找到当前连续 数字 的 连续个数
        for i in range(1, n):
            if (pressedKeys[i-1] == pressedKeys[i]):
                cnt += 1
            else:
                t = countDP(pressedKeys[i-1], cnt)
                ans *= t
                ans %= mod
                cnt = 1
        
        t = countDP(pressedKeys[-1], cnt)
        ans *= t
        ans %= mod
        return ans
