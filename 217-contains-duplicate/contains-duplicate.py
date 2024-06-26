class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = Counter(nums)
        for val in check.values():
            if val > 1:
                return True
        