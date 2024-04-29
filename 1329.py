# 1329. 将矩阵按对角线排序

from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        diag = [ [] for _ in range(m+n-1) ]

        for i in range(m):
            for j in range(n):
                diag[j-i].append( mat[i][j] )
        
        for each in diag:
            # 默认：reverse = False 升序
            # 此处用 降序
            each.sort(reverse = True)
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = diag[j-i].pop()
        
        return mat
