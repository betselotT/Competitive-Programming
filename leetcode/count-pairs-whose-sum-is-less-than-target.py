class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        j = 1
        count = 0
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if i < j:
                    sum = nums[i] + nums[j]
                    if sum < target:
                        count += 1
        return count