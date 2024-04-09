# 1103. 分糖果 II

class Solution:
    def distributeCandies(self, candies, num_people):
        ans = []
        n = int(pow(candies, 1/2))
        while (n*n + n < 2*candies):
            n += 1

        res = candies - (n*n - n)//2
        t = n // num_people
        m = n%num_people
        if not m:
            m = num_people
            t -= 1
        
        for i in range(num_people):

            if (i+1 < m):
                ans.append((i+1)*(t+1) + (t*t + t)//2*num_people)
            elif (i+1 == m):
                ans.append((i+1)*(t) + (t*t - t)//2*num_people + res)
            else:
                ans.append((i+1)*(t) + (t*t - t)//2*num_people)
        
        return ans
