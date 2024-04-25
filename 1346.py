# 1346. 检查整数及其两倍数是否存在

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        poss = set()
        for each in arr:
            if each in poss:
                return True
            else:
                if not (each & 1):
                    poss.add(each//2)
                poss.add(each*2)
        
        return False
