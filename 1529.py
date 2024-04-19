# 1529. 最少的后缀翻转次数

class Solution:
    def minFlips(self, target: str) -> int:
        ### solution 3: 继续优化， 相邻的字符是否变化
        if not target:
            return 0
        
        ans = 0
        pre = '0'
        
        for i in target:
            if pre != i:
                ans += 1
                pre = i

        return ans
        
        ### solution 2: 优化, 判断是否是连续的 '0' 还是连续的 '1'
        # if not target:
        #     return 0
        
        # ans = 0
        # isZero = '0'
        
        # for i in target:
        #     if isZero == i:
        #         continue
        #     else:
        #         ans += 1
        #         isZero = '1' if isZero == '0' else '0'
        # return ans

        ### solution 1: flag + 遍历
        # if not target:
        #     return 0
        
        # ans = 0

        # isZero = True
        
        # for i in target:
        #     if (isZero):
        #         if i == '0':
        #             continue
        #         else:
        #             ans += 1
        #             isZero = False
        #     else:
        #         if i == '1':
        #             continue
        #         else:
        #             ans += 1
        #             isZero = True
        # return ans
