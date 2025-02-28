# 3171. 找到按位或最接近 K 的子数组
import math
from typing import List


def minimumDifference(nums: List[int], k: int) -> int:
    # solution 2：双指针+滑动窗口

    # 遍历检查1.
    # nums数组中相邻的数字如果一样，则只保留一个
    # 遍历检查2.
    # k是否存在nums中
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1
        if (i < len(nums)) and (nums[i] == k):
            return 0
    
    min_diff = math.inf

    # 双指针，滑动窗口，当前值cur
    l = 0
    r = 0
    cur = 0

    # |= 操作，只要最后（最右边的一个数）某bit位为1，则，无论前面（左侧）删多少数都不会变化
    # 用一个list记录某bit位为1，滑动窗口中最后（右侧）的数的index
    # 最大整数为 32 bit位
    bit_1_max_index_in_nums = [-1] * 32
    
    # 滑动窗口，左端点固定，右端点右移，当前值cur只会越来越大
    while r < len(nums):
        # print("1", l,r,cur,min_diff)
        cur |= nums[r]
        min_diff = min(min_diff, abs(cur-k))

        # 更新滑动窗口中最后（右侧）的数的index，使list记录某bit位为1
        r_str = bin(nums[r])[2:]
        for ind,s in enumerate(r_str[::-1]):
            if s == '1':
                bit_1_max_index_in_nums[ind] = r
        # print(bit_1_max_index_in_nums)
        
        # 当前值cur大到大于k的时候，这个绝对差值也会越来越大
        # 这个时候要减小当前值cur，减小绝对差值，直到当前值cur小于k
        # 需要左端点右移，当前值cur只会越来越小
        while (l < r) and (cur > k):
            for j in range(32):
                if bit_1_max_index_in_nums[j] == l:
                    bit_1_max_index_in_nums[j] = -1
                    cur -= 2**j
            min_diff = min(min_diff, abs(cur-k))
            l += 1
            # print("2", l,r,cur,min_diff)
        r += 1
    return min_diff

    # solution 1：暴力双指针遍历 + 去重， 超时
    # i = 1
    # while i < len(nums):
    #     if nums[i] == nums[i-1]:
    #         nums.pop(i)
    #     else:
    #         i += 1

    # if k in nums:
    #     return 0

    # min_diff = math.inf
    # for l in range(len(nums)):
    #     cur = nums[l]
    #     cur_min_diff = abs(cur-k)
    #     visit = set([cur])
    #     r = l + 1
        
    #     while cur < k:
    #         if r == len(nums):
    #             break
    #         if nums[r] in visit:
    #             r += 1
    #             continue

    #         visit.add(nums[r])
    #         cur |= nums[r]
    #         cur_min_diff = min(cur_min_diff, abs(cur-k))
    #         r += 1
        
    #     min_diff = min([min_diff, abs(cur-k), cur_min_diff])
        
    # return min_diff

a = minimumDifference([6], 2)
print(a)
