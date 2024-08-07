class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        totalSum = sum(nums)
        if totalSum == x:
            return n
            
        target = totalSum - x
        hashmap = { 0: -1 }
        currLen, currSum = 0, 0
        for i in range(len(nums)):
            currSum += nums[i]
            j = hashmap.get(currSum - target, i)
            currLen = max(currLen, i - j)
            hashmap[currSum] = i

        return n - currLen if currLen > 0 else -1