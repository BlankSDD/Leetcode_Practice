# 2007. 从双倍数组中还原原数组

import collections
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ### solution 2: Counter + 升序
        if (len(changed) % 2):
            return []
        cnt = collections.Counter(changed)
        ans = []
        
        if (0 in cnt):
            if (cnt[0] % 2):
                return []
            else:
                ans += [0]*(cnt[0]//2)
                cnt[0] = 0

        for k in sorted(cnt.keys()):
            if cnt[k] == 0:
                continue
            
            if not (2*k in cnt):
                return []
            
            cnt[2*k] -= cnt[k]
            if cnt[2*k] < 0:
                return []

            ans += [k]*cnt[k]

            cnt[k] = 0
            
        if all([i == 0 for i in cnt.values()]):
            return ans
        else:
            return []
        
        ### solution 1: 倒序排序 + 一遍遍历
        # if (len(changed) % 2):
        #     return []
        # changed.sort(reverse = True)
        # m = changed[0]
        # f = [0] * (m+1)
        # ans = []
        # for i in changed:
        #     # 奇数
        #     if (i & 1):
        #         if (2*i > m) or ((2*i <= m) and (f[2*i] <= 0)):
        #             return []
        #         else:
        #             f[2*i] -= 1
        #             ans.append(i)
        #     # 偶数
        #     else:
        #         if (2*i <= m) and (f[2*i] >= 1):
        #             f[2*i] -= 1
        #             ans.append(i)
        #         else:
        #             f[i] += 1
            
        # if sum(f) == 0:
        #     return ans
        # else:
        #     return []
        
