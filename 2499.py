# 2499. 让数组不相等的最小总代价

from typing import List


class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        ### solutio 1: 分类讨论： 
        ### 以下所有 nums1 的值为 x, nums2 的值为 y
        ### 1. 找到所有重复的 index + 对应的值, 同时根据 值 计数
        ### 2. 在所有重复中, 一共有  swapCnt 重复对
        ###         出现最多的值: [mode值, modeCnt次数] (就是 众数)
        ### 3. 两种情况: (鸽巢原理)
        ### 3.1. modeCnt 没有超过 swapCnt 一半:
        ###         swapCnt 是偶数，那么两两交换即可
        ###         swapCnt 是奇数，交换会多一个，其中一个数必然可以和 nums1[0] 交换, 不需要多余的 费用
        ### 3.2. modeCnt 超过 swapCnt 一半:
        ###         无法通过重排这些数字，让数组不相等（还存在一些 mode 仍然相同）
        ###         此时需要遍历,从左到右(index从小到大),找到合适的进行交换
        ###         遍历完了还找不到,就 无法满足要求,返回 -1

        ans = 0

        n = len(nums1)
        need_change_index = []
        cnt = [0] * (n + 1)
        max_appear_times = 0
        max_appear_value = -1

        for i in range(n):
            cur = nums1[i]
            if (nums1[i] == nums2[i]):
                need_change_index.append(i)
                cnt[cur] += 1
                if cnt[cur] > max_appear_times:
                    max_appear_times, max_appear_value = cnt[cur], cur
        
        if (not need_change_index):
            return 0
        
        ans = sum(need_change_index)
        # 需要交换的数 的 值出现的最高次数 <= 需要换的次数的 1/2
        # 即可直接交换, 不会出现重复
        if (max_appear_times <= len(need_change_index)//2):
            return ans
        # 反之:
        # 需要交换的数 的 值出现的最高次数 > 需要换的次数的 1/2
        # 会出现重复 (鸽巢原理: 4或5个巢+3个鸽, 换之后,必有1个巢还是有鸽)
        # 此时: 从最小下标开始遍历,找到需要更换的
        
        still_need_change_num = 2*max_appear_times - len(need_change_index)
        still_need_change_value = max_appear_value

        for i in range(n):
            # 遍历时保证: 
            # 2个list不同的 (不需要 查找 是否在 need_change_index 中)
            # nums1[i] != 出现最多
            # 出现最多 != nums2[i]
            if (nums1[i] != nums2[i]) and (nums1[i] != still_need_change_value) and (still_need_change_value != nums2[i]):
                ans += i
                still_need_change_num -= 1
                if (not still_need_change_num):
                    break
        
        if still_need_change_num:
            return -1
        else:
            return ans




