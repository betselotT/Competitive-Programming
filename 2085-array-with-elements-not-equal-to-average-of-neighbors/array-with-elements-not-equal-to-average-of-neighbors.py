class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        i= 0 
        j= len(nums) - 1
        while i < j:
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j -= 1
            
        if len(res) != len(nums):
            res.append(nums[i])
        return res