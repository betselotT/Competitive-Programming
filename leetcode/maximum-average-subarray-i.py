class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        mx = curr / k

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            mx = max(mx, curr / k)
        return mx