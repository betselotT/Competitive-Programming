class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(num, path, sum):
            if sum == target:
                arr.add(tuple(sorted(path)))
                return
            if sum > target:
                return
            for i in range(num, len(candidates)):
                if i > num and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, sum + candidates[i])
                path.pop()

        arr = set()
        backtrack(0, [], 0)
        return (arr)