# 2225. 找出输掉零场或一场比赛的玩家

from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ### solution 2: 3个set分别为输0，1，多次
        lose_0 = set()
        lose_1 = set()
        lose_more = set()
        for w,l in matches:
            if (not w in lose_1) and (not w in lose_more):
                lose_0.add(w)
            
            if (not l in lose_1) and (not l in lose_more):
                lose_0.discard(l)
                lose_1.add(l)
            elif (l in lose_1):
                lose_1.discard(l)
                lose_more.add(l)
        
        return [sorted(list(lose_0)),  sorted(list(lose_1))]


        ### solution 1: 计数输赢次数，遍历查找，二分插入
        # ans = [[], []]
        # cnt = defaultdict(list)
        # for w,l in matches:
        #     if (not w in cnt):
        #         cnt[w] = [1,0]
        #     else:
        #         cnt[w][0] += 1
        #     if (not l in cnt):
        #         cnt[l] = [0,1]
        #     else:
        #         cnt[l][1] += 1

        # for k,w_l in cnt.items():
        #     if w_l[1] == 0:
        #         i = bisect.bisect_left(ans[0], k)
        #         ans[0].insert(i, k)
        #     elif w_l[1] == 1:
        #         i = bisect.bisect_left(ans[1], k)
        #         ans[1].insert(i, k)
        
        # return ans
