class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arrX, rangeX = 0, 0
        for i, num in enumerate(nums):
            arrX ^= num
            rangeX ^= i + 1
        
        return rangeX ^ arrX