# 2903. 找出满足差值条件的下标 I

from math import inf
from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ### solution 2: 优化，只用维护从一侧开始的最大，最小值
        n = len(nums)
        
        if (indexDifference >= n):
            return [-1, -1]
        if (valueDifference == 0):
            return [0,indexDifference]

        max_idx, min_idx = 0, 0

        for j in range(indexDifference, n):
            i = j-indexDifference
            if nums[i] > nums[max_idx]:
                max_idx = i
            elif nums[i] < nums[min_idx]:
                min_idx = i
            
            if (abs(nums[j] - nums[max_idx]) >= valueDifference):
                return [max_idx, j]
            if (abs(nums[j] - nums[min_idx]) >= valueDifference):
                return [min_idx, j]
        
        return [-1, -1]


        ### solution 1: 双队列，一个从左开始，一个从右开始，维护最大最小值以及他们的index, 这个方法复杂化了
        # n = len(nums)
        
        # if (indexDifference >= n):
        #     return [-1, -1]
        # if (valueDifference == 0):
        #     return [0,indexDifference]

        
        # l = [[nums[0], 0, nums[0], 0]]
        # r = [[nums[-1], n-1, nums[-1], n-1]]
        

        # for i in range(1, n):
        #     l_cur = nums[i]
        #     l_tmp = []
        #     if l_cur < l[-1][0]:
        #         l_tmp.append( l_cur )
        #         l_tmp.append( i )
        #     else:
        #         l_tmp.append( l[-1][0] )
        #         l_tmp.append( l[-1][1] )
        #     if l_cur > l[-1][2]:
        #         l_tmp.append( l_cur )
        #         l_tmp.append( i )
        #     else:
        #         l_tmp.append( l[-1][2] )
        #         l_tmp.append( l[-1][3] )
        #     l.append(l_tmp)
            
        #     r_cur = nums[-1-i]
        #     r_tmp = []
        #     if r_cur < r[-1][0]:
        #         r_tmp.append( r_cur )
        #         r_tmp.append( n-i-1 )
        #     else:
        #         r_tmp.append( r[-1][0] )
        #         r_tmp.append( r[-1][1] )
        #     if r_cur > r[-1][2]:
        #         r_tmp.append( r_cur )
        #         r_tmp.append( n-i-1 )
        #     else:
        #         r_tmp.append( r[-1][2] )
        #         r_tmp.append( r[-1][3] )
        #     r.append(r_tmp)
        
        # r.reverse()

        # for i in range(indexDifference, n):

        #     if (abs( l[i-indexDifference][0] - r[i][2] ) >= valueDifference):
        #         return [l[i-indexDifference][1], r[i][3]]
        #     if (abs( l[i-indexDifference][2] - r[i][0] ) >= valueDifference):
        #         return [l[i-indexDifference][3], r[i][1]]
            
        # return [-1, -1]
