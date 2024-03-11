class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k = []
        n = len(arr)
        for i in range(n):
            mx = max(arr[:n - i])
            mx_idx = arr.index(mx) + 1
            arr[:mx_idx] = reversed(arr[:mx_idx])
            k.append(mx_idx)
            arr[:n - i] = reversed(arr[:n - i])
            k.append(n - i)
        return k