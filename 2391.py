# 2391. 收集垃圾的最少总时间

from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ### solution 2: 只有最后没有该种垃圾，对应车就不用过来了，用全程做减法
        ans = sum( [len(each) for each in garbage] ) + 3 * sum( travel )
        t = 0
        mf, pf, gf = False,False,False
        travel.insert(0, 0)

        for each in reversed(garbage):
            t += 1
            lastt = travel[-t]
            
            if (not mf):
                if ('M' in each):
                    mf = True
                else:
                    ans -= lastt
            if (not pf):
                if ('P' in each):
                    pf = True
                else:
                    ans -= lastt
            if (not gf):
                if ('G' in each):
                    gf = True
                else:
                    ans -= lastt
        
        return ans

        ### solution 1: 暴力遍历
        # n = len(garbage)

        # ans = 0
        # Mstopnext, Pstopnext, Gstopnext = 0,0,0

        # for i in range(n):
        #     ans += len(garbage[i])
        #     tmp = collections.Counter(garbage[i])

        #     if tmp['M']:
        #         ans += Mstopnext
        #         Mstopnext = 0
        #     if tmp['P']:
        #         ans += Pstopnext
        #         Pstopnext = 0
        #     if tmp['G']:
        #         ans += Gstopnext
        #         Gstopnext = 0
            
        #     if i < n-1:
        #         Mstopnext += travel[i]
        #         Pstopnext += travel[i]
        #         Gstopnext += travel[i]
        
        # return ans
            
            
             
