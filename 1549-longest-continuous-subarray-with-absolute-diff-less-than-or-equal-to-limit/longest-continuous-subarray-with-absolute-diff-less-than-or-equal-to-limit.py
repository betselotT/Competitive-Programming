from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ml = SortedList()
        i, ans = 0, 0
        for num in nums:
            ml.add(num)
            while ml[-1] - ml[0] > limit:
                ml.remove(nums[i])
                i += 1
            ans = max(ans, len(ml))
        return ans