class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_nums = []
        count = 0
        num = 1
        while count != k:
            if num not in arr:
                missing_nums.append(num)
                count += 1
            num += 1
        return missing_nums[-1]