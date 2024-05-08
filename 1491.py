# 1491. 去掉最低工资和最高工资后的工资平均值

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary)-2)
