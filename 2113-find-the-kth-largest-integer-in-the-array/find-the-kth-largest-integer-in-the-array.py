class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(num) for num in nums]
        nums.sort(reverse=True)
        return str(nums[k - 1])