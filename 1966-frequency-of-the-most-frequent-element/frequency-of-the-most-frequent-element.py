class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        maxx = 0
        summ = 0

        for r in range(len(nums)):
            summ += nums[r]

            while (nums[r] * (r - l + 1)) - summ > k:
                summ -= nums[l]
                l += 1
            maxx = max(maxx, r - l + 1)

        return maxx
