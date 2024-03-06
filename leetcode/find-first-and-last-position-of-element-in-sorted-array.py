class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        ans1 = -1
        ans2 = -1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                ans1 = mid
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                ans2 = mid
                low = mid + 1
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return [ans1, ans2]