class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictt = Counter(nums)
        n = len(nums)
        for key, val in dictt.items():
            if val > (n // 2):
                return key
            