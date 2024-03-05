class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(num, path, sum):
            if sum == target:
                arr.append(path[:])
                return
            if sum > target:
                return
            for i in range(num,len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, sum + candidates[i])
                path.pop()

        arr = []
        backtrack(0, [], 0)
        return (arr)