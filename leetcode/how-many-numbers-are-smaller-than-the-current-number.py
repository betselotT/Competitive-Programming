class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        sortedNums = sorted(nums)
        dic = {}
        for i in range(len(sortedNums)):
            if sortedNums[i] not in dic:
                dic[sortedNums[i]] = i
        for i in nums:
            result.append(dic[i])
        return result