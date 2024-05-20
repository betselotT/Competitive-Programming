class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = 0
        for num in nums:
            n ^= num
        c = n & (-n)

        num1 = 0
        num2 = 0
        
        for num in nums:
            if num & c:
                num1 ^= num  
            else:
                num2 ^= num 
        
        return [num1, num2]