class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mySet=set()
        for i in nums:
            if i in mySet:
                return i
            else:
                mySet.add(i)