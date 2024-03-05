class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        prev = None
        nums.sort()
        def backtrack(num, path):
            nonlocal prev
            arr.append(path[:])

            for i in range(num, len(nums)):
                if prev == nums[i]: 
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                prev = path.pop()


        arr = []
        backtrack(0, [])
        return arr