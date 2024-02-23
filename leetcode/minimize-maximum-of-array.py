class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans=0
        ps=0
        for i in range(len(nums)):
            ps+=nums[i]
            if nums[i]>=ans:
                ans= max(ans,ceil(ps/(i+1)))
        return ans
            