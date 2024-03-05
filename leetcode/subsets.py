class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(num, path):
            arr.append(path[:])

            for i in range(num, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()


        arr = []
        backtrack(0, [])
        return arr