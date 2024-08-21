class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        
        for num in nums:
            remainder = num % 3
            if remainder == 1:
                count += 1
            elif remainder == 2:
                count += 1
        
        return count