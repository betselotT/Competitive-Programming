class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictt = Counter(nums)
        for key, val in dictt.items():
            if val == 1:
                return key