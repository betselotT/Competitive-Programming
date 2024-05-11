class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        def dp(i, summ):
            if (i, summ) in memo:
                return memo[(i,summ)]
            if i == len(nums):
                if summ == target:
                    return 1
                else:
                    return 0
            
            memo[(i,summ)] =  dp(i + 1, summ + nums[i]) + dp(i + 1, summ - nums[i])
            return memo[(i, summ)]

        return dp(0, 0)