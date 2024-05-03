class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = 0
        for num in nums:
            x ^= num
        
        x ^= k
        return x.bit_count()