class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        def check(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if i not in memo:
                memo[i] = max(nums[i] + check(i - 2), check(i - 1))
            
            return memo[i]
        
        return check(len(nums) - 1)