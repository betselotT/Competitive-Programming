class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prevRow = self.getRow(rowIndex - 1)
        curr = [1] * (rowIndex + 1)
        for j in range(1, len(curr) - 1):
            curr[j] = prevRow[j - 1] + prevRow[j]
        return curr
