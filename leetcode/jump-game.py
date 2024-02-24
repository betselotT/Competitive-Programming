class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maximum = 0
        for i in range(n):
            if i > maximum: 
                return False
            maximum = max(maximum, i + nums[i])
            if maximum >= n - 1:
                return True
        return False
