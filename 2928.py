# 2928. 给小朋友们分糖果 I

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ### solution 3: 暴力遍历
        ans = 0
        for i in range(limit+1):
            for j in range(limit+1):
                if i + j > n:
                    break
                if n - i - j <= limit:
                    ans += 1
        
        return ans
        
        ### solution 2: 判断 n 与 limit 的关系， 优化
        # ans = 0
        # if n <= 3*limit:
        #     for i in range(max(0, n-2*limit), min(n+1, limit+1)):
        #         if n-i <= limit:
        #             ans += (n-i+1)
        #         else:
        #             ans += (2*limit - n+i + 1)
        #     return ans
        # else:
        #     return 0

        ### solution 1: 判断 n 与 limit 的关系
        # ans = 0
        # if n <= limit:
        #     for i in range(n+1):
        #         ans += 1 * (n-i+1)
        #     return ans              # (n+2)*(n+1) // 2

        # elif n <= 2*limit:
        #     for i in range(limit+1):
        #         if n-i <= limit:
        #             ans += 1 * (n-i+1)
        #         else:
        #             ans += 1 * (limit - (n-i-limit) + 1)
        #     return ans

        # elif n <= 3*limit:
        #     for i in range(n-2*limit, limit+1):
        #         if n-i <= limit:
        #             ans += 1 * (n-i+1)
        #         elif n-i <= 2*limit:
        #             ans += 1 * (limit - (n-i-limit) + 1)
        #     return ans

        # else:
        #     return 0
        
        
