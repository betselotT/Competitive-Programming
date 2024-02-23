class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        myDict = Counter(nums)
        checker = set(nums)
        maximum = max(nums)
        for i in range(maximum):
            if i not in checker:
                return i
        return maximum + 1