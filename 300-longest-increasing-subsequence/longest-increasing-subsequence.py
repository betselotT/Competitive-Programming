class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        def dp(i):
            if i >= len(nums):
                return 0
            
            if memo[i] == 0:
                memo[i] = 1
                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i]:
                        memo[i] = max(1 + dp(j), dp(i))
            
            return memo[i]

        maxx = 0
        for i in range(len(nums)):
            maxx = max(maxx, dp(i))
        
        return maxx