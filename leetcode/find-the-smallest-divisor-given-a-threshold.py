class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calc(mid, threshold):
            count = 0
            for i in range(len(nums)):
                count += ceil(nums[i] / mid)
            if count > threshold:
                return False
            return True

        low = 1
        high = max(nums)
        while low <= high:
            mid = (low + high) // 2
            if calc(mid, threshold):
                high = mid - 1
            else:
                low = mid + 1
        return low