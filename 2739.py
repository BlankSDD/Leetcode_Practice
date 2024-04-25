# 2739. 总行驶距离

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = mainTank
        while (mainTank >= 5) and (additionalTank > 0):
            tmp = min(additionalTank, mainTank//5)
            
            mainTank = mainTank % 5 + tmp
            additionalTank -= tmp

            ans += tmp
        
        return ans * 10
