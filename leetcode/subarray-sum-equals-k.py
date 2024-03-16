class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        myDict = defaultdict(int)
        myDict[0] = 1
        count = 0
        sum_ = 0
        for i in nums:
            sum_ += i
            if sum_ - k in myDict:
                count += myDict[sum_ - k]
            myDict[sum_] += 1

        return count