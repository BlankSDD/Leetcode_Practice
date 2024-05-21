# 2644. 找出可整除性得分最大的整数

from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        
        # 降序，比 divisor 小就不可能了，可以 break
        nums.sort(reverse = True)

        min_ans = inf
        max_num_d = -inf

        for d in divisors:
            tmp = 0
            for each in nums:
                if each < d:
                    break
                if not (each%d):
                    tmp += 1
            
            if (tmp > max_num_d) or ((tmp == max_num_d) and (d < min_ans)):
                min_ans = d
                max_num_d = tmp
        
        return min_ans
