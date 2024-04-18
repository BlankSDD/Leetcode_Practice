# 139. 单词拆分

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ### solution 2: dp
        dp = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for w in wordDict:
                wn = len(w)
                if (i >= wn) and (s[i-wn : i] == w):
                    dp[i] |= dp[i-wn]
                    if dp[i]:
                        break
            
            if dp[-1]:
                return True
        
        return dp[-1]

        ### solution 1: 暴力递归，超时
        # if not s:
        #     return True
        # ans = False
        # for w in wordDict:
        #     if s[:len(w)] == w:
        #         ans |= self.wordBreak(s[len(w):], wordDict)
        # return ans
