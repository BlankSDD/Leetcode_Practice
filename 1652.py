# 1652. 拆炸弹

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = []

        if k == 0:
            return [0] * n
        elif k > 0:
            l = 1
            r = k
            tmp = sum(code[1:k+1])
        else:
            l = n+k
            r = n-1
            tmp = sum(code[n+k:])
        
        for i in range(n):
            ans.append(tmp)
            tmp -= code[l]
            l += 1
            l %= n
            r += 1
            r %= n
            tmp += code[r]
        return ans
