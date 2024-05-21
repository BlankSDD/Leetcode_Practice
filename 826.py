# 826. 安排工作以达到最大收益

from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ### solution 1: 双指针遍历，工人能力排序，工作难度排序，双指针找出当前工人可以完成的所有工作中利润最大的工资

        ### 按照难度排序， 升序（default reverse = False 升序）
        d_p = sorted(zip(difficulty, profit),key=lambda x:x[0])
        
        ### 工人能力排序，升序
        worker.sort()

        i = 0
        j = 0
        cur_max_salary = 0
        ans = 0

        for w in worker:
            while (i < len(difficulty)) and (d_p[i][0] <= w):
                cur_max_salary = max(cur_max_salary, d_p[i][1])
                i += 1
            else:
                ans += cur_max_salary

        return ans
