class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        left, i, count = 0, 0, 0
        for j in range(len(nums)):
            while i <= left:
                count += nums[i]
                i += 1
            arr.append(count)
            left += 1
        return arr