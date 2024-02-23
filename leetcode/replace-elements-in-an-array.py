class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        myDict = defaultdict(int)
        for i, value in enumerate(nums):
            myDict[value] = i
        for i, j in operations:
            nums[myDict[i]] = j
            myDict[j] = myDict[i]
        return nums