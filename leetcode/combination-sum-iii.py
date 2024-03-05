class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        arr = []
        
        def backtrack(i):
            if len(path) == k and sum(path) == n:
                arr.append(path[:])
                return 

            for j in range(i + 1, 10):
                if sum(path) < n:
                    path.append(j)
                    backtrack(j)
                    path.pop()
        backtrack(0)
        return arr