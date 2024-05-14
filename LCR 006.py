# LCR 006. 两数之和 II - 输入有序数组

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ### solution 2: dict 记录 + 做减法查找
        num_index = dict()
        for i, x in enumerate(numbers):
            if target-x < numbers[0]:
                return [-1, -1]

            if target-x in num_index:
                return [num_index[target-x], i]
            else:
                num_index[x] = i


        ### solution 1: 二分查找 + 双指针
        # i = 0
        # j = bisect.bisect_right(numbers, target-numbers[0])
        
        # n = len(numbers)

        # if (j == n):
        #     j -= 1
        
        # while i < j:
        #     if numbers[i] + numbers[j] == target:
        #         return [i,j]
        #     elif numbers[i] + numbers[j] < target:
        #         i += 1
        #     else:
        #         j -= 1

        # return [-1, -1]
