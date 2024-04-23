# 2829. k-avoiding 数组的最小总和

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        if (n <= k//2):
            return (1+n)*n//2

        ans = (1 + k//2)*(k//2)//2
        ans += (k + k+n-k//2-1)*(n-k//2)//2

        return ans
        
