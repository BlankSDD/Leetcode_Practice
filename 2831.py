from collections import defaultdict
from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        ### solution 1: 哈希表记录每个数字出现的所有index形成list
        ###             遍历哈希表的 values, 
        ###             双指针 i,j 遍历当前 value ,
        ###             遍历 j：
        ###                 while 删除多于 k， i+=1
        ###                 更新最大连续数量
        n = len(nums)
        num_index = defaultdict(list)
        for i in range(n):
            num_index[nums[i]].append(i)

        ans = 1
        for v in num_index.values():
            if len(v) <= ans:
                continue
            
            i = 0
            cur_ans = 1
            for j in range(1, len(v)):
                while (i < j) and ((v[j] - v[i]) - (j-i) > k):
                    i += 1
                
                cur_ans = max(cur_ans, j-i+1)

            ans = max(ans, cur_ans)
        
        return ans
            
