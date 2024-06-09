class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maxx = (1 << maximumBit) - 1
        check = [0] * len(nums)
        
        check[0] = nums[0]
        for i in range(1, len(nums)):
            check[i] = check[i - 1] ^ nums[i]
        
        ans = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = check[i] ^ maxx
        
        ans.reverse()
        return ans