# 852. 山脉数组的峰顶索引

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        m = (l+r) // 2
        while True:
            if (arr[m-1] < arr[m]) and (arr[m] > arr[m+1]):
                return m
            elif (arr[m-1] < arr[m]):
                l = m
            elif (arr[m] > arr[m+1]):
                r = m
            m = (l+r) // 2
        
        return m
