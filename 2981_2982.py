# 2981. 找出出现至少三次的最长特殊子字符串 I
# 2982. 找出出现至少三次的最长特殊子字符串 II
# 两题完全一样

from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        ### solution 1: 遍历一遍，哈希 + 排序 + 分类讨论
        n = len(s)
        if n <= 2:
            return -1

        cnt = defaultdict(list)
        tmp = 1
        pre = s[0]
        for i in range(1, n):
            if pre == s[i]:
                tmp += 1
            else:
                cnt[pre].append(tmp)
                tmp = 1

            pre = s[i]

        cnt[pre].append(tmp)

        ans = -1
        for v in cnt.values():
            v.sort(reverse=True)
            
            ### [5, x, x] or [5, x] or [5]
            if v[0] >= 3:
                ans = max(ans, v[0]-2)

            if len(v) >= 3:
                ### [6, 5, x]
                if v[0] > v[1]:
                    ans = max(ans, v[1])
                
                ### [5, 5, x]
                else:

                    ### [5, 5, 5]
                    if v[1] == v[2]:
                        ans = max(ans, v[2])
                    
                    ### [5, 5, 3]
                    else:
                        ans = max(ans, v[1]-1)
            
            elif len(v) == 2:

                ### [1, 1]
                if sum(v) < 3:
                    continue

                ### [6, 5]
                if v[0] > v[1]:
                    ans = max(ans, v[1])
                
                ### [6, 6]
                else:
                    ans = max(ans, v[1]-1)

        return ans
