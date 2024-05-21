class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(tar):
            if tar == target:
                return 1
            if tar > target:
                return 0
            if tar not in memo:
                count = 0
                for num in nums:
                    count += dp(tar + num)
                memo[tar] = count
        
            return memo[tar]
        return dp(0)