class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if int(str(a) + str(b)) < int(str(b) + str(a)):
                return 1
            elif int(str(a) + str(b)) == int(str(b) + str(a)):
                return 0
            else:
                return -1
        nums.sort(key = cmp_to_key(compare))
        if all(i == 0 for i in nums):
            return "0"
        return "".join(str(i) for i in nums)