class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        numsStr = []
        for i in range(len(nums)):
            numsStr.append(str(nums[i]))
        ans = []
        for i in range(len(numsStr)):
            for j in range(len(numsStr[i])):
                ans.append(int(numsStr[i][j]))
        
        return ans