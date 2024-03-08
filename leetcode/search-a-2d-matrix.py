class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            low = 0
            high = len(matrix[i]) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[i][mid] < target:
                    low = mid + 1
                elif matrix[i][mid] > target:
                    high = mid - 1
                elif matrix[i][mid] == target:
                    return True