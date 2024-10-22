class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mydictt = Counter(nums)
        summ = 0
        for key, val in mydictt.items():
            if val == 1:
                summ += key
        
        return summ