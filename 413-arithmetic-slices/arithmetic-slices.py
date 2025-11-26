class Solution:
    def f(self, length: int) -> int: 
        return (length - 1) * (length - 2) // 2
    
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        i = 1
         
        while i < n:
            l = i - 1   
            r = i       
            d = nums[r] - nums[l] 
            
            while r < n and nums[r] - nums[r - 1] == d:
                r += 1
                
            length = r - l   
            sum_val = self.f(length)  
            cnt = (cnt + sum_val) 
             
            i = r 
            
        return cnt