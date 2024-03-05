class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first_num, path):
            if len(path) == k:
                arr.append(path[:])
                return
            for num in range(first_num, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()
        arr = []
        backtrack(1, [])
        return arr