class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        F0 = 0
        _sum = 0
        i = 0
        while(i < len(nums)):

            _sum += nums[i]
            F0 += i * nums[i]
            i += 1
        
        prev = _max = F0
        i = 1
        while(i < len(nums)):

            Fi = prev + (_sum - nums[len(nums) - i]) - (len(nums) - 1) * nums[len(nums) - i]

            if(Fi > _max):
                _max = Fi
            prev = Fi
            i += 1

        return _max