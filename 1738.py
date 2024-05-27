# 1738. 找出第 K 大的异或坐标值

from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        ### solution 1: dp
        m = len(matrix)
        n = len(matrix[0])
        pre = [[0]*(n+1) for _ in range(m+1)]
        all_num = []

        # i,j 为 matrix 中 实际 index + 1
        # 为什么要 +1：
        # 对于[1][1]: 0^0^0^matrix[0][0] 则为 matrix 本身
        # 0 异或 任何数 为其本身： 0*a = a
        for i in range(1, m+1):
            for j in range(1, n+1):
                ### 状态转移公式 为什么是 ：pre[i][j] = 上方pre[i-1][j] ^ 左侧pre[i][j-1] ^ 左上方pre[i-1][j-1] ^ 该数本身matrix[i-1][j-1]
                ### 1. 异或 左侧 + 上方 的
                ### 但是 左侧   异或过 左上方的
                ###      上方 也异或过 左上方的
                ### 左上方的被异或过两次，抵消了 ： (a^c) ^ (b^c) = a^b
                ### 2. 所以 要再一次 异或 左上方的
                pre[i][j] = pre[i-1][j] ^ pre[i][j-1] ^ pre[i-1][j-1] ^ matrix[i-1][j-1]
                all_num.append(pre[i][j])

        return sorted(all_num)[-k]

                
