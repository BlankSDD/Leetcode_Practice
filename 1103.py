# 1103. 分糖果 II

class Solution:
    def distributeCandies(self, candies, num_people):
        ### solution 2: 暴力模拟
        # ans = [0] * num_people
        # i = 0
        # cur = 1
        # while candies > 0:
        #     ans[i] += cur
        #     candies -= cur

        #     i += 1
        #     i %= num_people
            
        #     cur = min(cur+1, candies)

        # return ans

        ### solution 1: 数学计算
        ### 1.必然是 1+2+...+n+ res = candies
        ### 2.算出 n 与 res
        ### 3. n = num_people * t + m
        ### 即：分配经历了 t 整个循环
        ###     在第 t+1 个循环中，仅有前 m 个人有分到东西
        ###     注意： m 可取 num_people
        ###           就算刚好除尽， t 需 -1
        ### 4.
        ans = []

        # 2.算出 n 与 res
        n = int(pow(candies, 1/2))
        while (n*n + n < 2*candies):
            n += 1

        res = candies - (n*n - n)//2

        # 3. 算出 t 和 m ： n = num_people * t + m
        t = n // num_people
        # 在第 t+1 个循环中，仅有前 m 个人有分到东西
        m = n%num_people
        # m 可取 num_people ，就算刚好除尽， t 需 -1
        if not m:
            m = num_people
            t -= 1
        
        # 根据循环数 t 和 余数 m 分配
        # [ x , x , x , x ,                    x , x , x , x]
        #   |   |   |   | 最后一轮的前 m-1 个
        #                                      | 最后一轮的第 m 个（整个分配的最后一个）
        for i in range(num_people):
            # 最后一轮的前 m-1 个
            # 多加一轮分配
            if (i+1 < m):
                ans.append((i+1)*(t+1) + (t*t + t)//2*num_people)
            # 最后一轮的第 m 个（整个分配的最后一个）
            # 多加最后剩余的
            elif (i+1 == m):
                ans.append((i+1)*(t) + (t*t - t)//2*num_people + res)
            # 未参与最后一轮的
            # 没有多加的
            else:
                ans.append((i+1)*(t) + (t*t - t)//2*num_people)
        
        return ans
