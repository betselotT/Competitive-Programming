class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n <= 4:
            return  0 

        ans = min(nums[-1] - nums[3], nums[n-4] - nums[0])
        ans = min(ans, nums[n-2] - nums[2])
        ans = min(ans, (nums[n-3] - nums[1]))
        
        return ans