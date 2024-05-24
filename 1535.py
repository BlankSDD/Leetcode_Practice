# 1535. 找出数组游戏的赢家1542.py

from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cur = arr[0]
        continus_win = 0
        for each in arr[1:]:
            if cur > each:
                continus_win += 1
            else:
                cur = each
                continus_win = 1
            if (continus_win == k):
                return cur
        
        return cur
                
