# 2901. 最长相邻不相等子序列 II

from collections import defaultdict
from typing import List



### solution 2: 优化 空间存储，只记录 上一个节点
def verify_hanming_dist_is_1(x, y):
    d = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            d += 1
        if d >= 2:
            return -1
    return d

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        
        tmp = defaultdict(list)
        
        for i in range(n):
            tmp[len(words[i])].append( [i, words[i]] )
        
        m = 0
        ans = []
        for ind_w_list in sorted(tmp.values(), key=lambda x:len(x), reverse=True):
            if (m >= len(ind_w_list)):
                break

            dp = [1] * len(ind_w_list)
            parents = dict()

            for i in range(len(ind_w_list)):
                i_ind,i_w = ind_w_list[i]

                for j in range(i-1, -1, -1):
                    j_ind, j_w = ind_w_list[j]
                    
                    if (dp[j] < dp[i]):
                        continue
                    
                    if (groups[i_ind] != groups[j_ind]) and (verify_hanming_dist_is_1(i_w, j_w) == 1):
                        
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            parents[i_w] = j_w
                        
                if m < dp[i]:
                    m = dp[i]
                    ans = [i_w]

            f = ans[0]
            while f in parents:
                f = parents[f]
                ans = [f] + ans
        
        return ans









### solution 1: 记录和传递 整个子序列
# def verify_hanming_dist_is_1(x, y):
#     d = 0
#     for i in range(len(x)):
#         if x[i] != y[i]:
#             d += 1
#         if d >= 2:
#             return -1
#     return d

# class Solution:
#     def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
#         n = len(words)
        
#         tmp = defaultdict(list)
        
#         for i in range(n):
#             tmp[len(words[i])].append( [i, words[i]] )
        
#         m = 0
#         ans = []
#         for ind_w_list in sorted(tmp.values(), key=lambda x:len(x), reverse=True):
#             if (m >= len(ind_w_list)):
#                 break

#             dp = [ [1, []] for _ in range(len(ind_w_list)) ]
            
#             for i in range(len(ind_w_list)):
#                 i_ind,i_w = ind_w_list[i]
#                 dp[i] = [1, [i_w]]

#                 for j in range(i-1, -1, -1):
#                     j_ind, j_w = ind_w_list[j]

#                     if (dp[j][0] < dp[i][0]):
#                         continue
                    
#                     if (groups[i_ind] != groups[j_ind]) and (verify_hanming_dist_is_1(i_w, j_w) == 1):
                        
#                         if dp[j][0] + 1 > dp[i][0]:
#                             dp[i][0] = dp[j][0] + 1
#                             dp[i][1] = dp[j][1][:] + [words[i_ind]]
                        
#                 if m < dp[i][0]:
#                     m = dp[i][0]
#                     ans = dp[i][1]
        
#         return ans



