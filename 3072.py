# 3072. 将元素分配到两个数组中 II

import bisect
from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        ### solution 1: 模拟遍历 + 维持两个排序 tmp1, tmp2 + 分别二分插入找到大于当前nums[i]的数量 + 插入arr1, arr2, tmp1, tmp2
        ### 由于 bisect 只能用于 升序 序列，greaterCount 是大于 nums[i] 的值的数量，所以 排序 tmp1, tmp2, 使用的是 负数 排序， bisect_left 得到的结果就是 大于 nums[i] 的值的数量
        n = len(nums)
        arr1, arr2 = [nums[0]], [nums[1]]
        tmp1 = [-nums[0]]
        tmp2 = [-nums[1]]

        for each in nums[2:]:
            index1 = bisect.bisect_left(tmp1, -each)
            index2 = bisect.bisect_left(tmp2, -each)
            if (index1 > index2) or ((index1 == index2) and len(tmp1) <= len(tmp2)):
                arr1.append(each)
                tmp1.insert(index1, -each)
            else:
                arr2.append(each)
                tmp2.insert(index2, -each)
        
        return arr1 + arr2
            


