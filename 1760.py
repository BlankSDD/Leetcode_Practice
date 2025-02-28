import bisect
from collections import Counter
import math
from typing import List

def minimumSize(nums: List[int], maxOperations: int) -> int:
    # solution 1: 二分法遍历所有答案，检验答案是否符合，直接用大于答案的数来分割即可
    nums = [x for x in nums if x != 1]
    if maxOperations >= sum(nums):
        return 1
    num_cnt = Counter(nums)
    order_key = sorted(num_cnt.keys(), reverse=True)
    cur_min_cost_l = order_key[0]
    cur_min_cost_r = -cur_min_cost_l + 2
    mid = (cur_min_cost_l + cur_min_cost_r) // 2
    cur_maxOper = 0
    while cur_min_cost_l > cur_min_cost_r:
        cur_maxOper = 0
        mid = (cur_min_cost_l + cur_min_cost_r) // 2
        for k in order_key:
            if k > mid:
                cur_maxOper += num_cnt[k] * int((k-0.5) // mid)
            else:
                break
        if cur_maxOper > maxOperations:
            if mid == cur_min_cost_r:
                break
            cur_min_cost_r = mid
        else:
            cur_min_cost_l = mid

    return cur_min_cost_l

