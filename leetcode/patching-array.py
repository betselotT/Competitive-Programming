class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        target = 1
        ans = 0
        i = 0
        while target <= n:
            if i < len(nums) and target >= nums[i]:
                target += nums[i]
                i += 1
            else:
                target *= 2
                ans += 1 
        return ans