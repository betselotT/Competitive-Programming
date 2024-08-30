class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = nums[-1]
        while k > 1:
            nums[-1] += 1
            m += nums[-1]
            k -= 1
        
        return m