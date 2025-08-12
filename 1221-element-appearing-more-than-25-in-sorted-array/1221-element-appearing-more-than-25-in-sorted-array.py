class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ahead = len(arr) // 4

        for i in range(len(arr) - ahead):
            if arr[i] == arr[i + ahead]:
                return arr[i]