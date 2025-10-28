class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        trimmed = arr[len(arr) // 20 : -len(arr) // 20]
        return sum(trimmed) / len(trimmed)