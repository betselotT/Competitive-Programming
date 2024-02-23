from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        count = 0
        i, j = 0, 0
        while i < n:
            count += mat[i][j]
            i += 1
            j += 1
        i, j = 0, n - 1
        while i < n:
            if i != j:
                count += mat[i][j]
            i += 1
            j -= 1
        return count
