# LCR 003. 比特位计数

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ### solution 2: 同理solution 1，dp + 最低有效位 
        ### 例如： 5 -> 101
        ###        2 -> 10
        ### 则， 加上最低位的 bit 1 后，5 只比 2 多一个 bit 1
        ### 即， dp[5] = dp[5>>2] + 1
        if n == 0:
            return [0]

        dp = [0]
        for i in range(1, n+1):

            # 判断 i 的最低位是否为 1
            # if (i&1):
            #     dp.append( dp[i>>1] + 1 )
            # else:
            #     dp.append( dp[i>>1] )

            # 优化判断
            dp.append( dp[i>>1] + (i&1) )

        return dp
        
        
        
        ### solution 1: dp + 最高有效位 
        ### 例如： 5 -> 101
        ###        1 ->  01
        ### 则， 减去最高位的 bit 1 后，5 只比 1 多一个 bit 1
        ### 即， dp[5] = dp[5 - 2**2] + 1
        # if n == 0:
        #     return [0]

        # dp = [0]
        # highbit = 0
        # for i in range(1, n+1):
            
        #     # 判断 i 是否为 2 的整 x 次方,
        #     # i 是递增的， i 的二进制数的位数会 增加
        #     # 每到一个 2 的整 x 次幂，二进制位数 + 1
        #     if (i&(i-1) == 0):
        #         highbit = i
            
        #     dp.append( dp[i-highbit] + 1 )
        # return dp
