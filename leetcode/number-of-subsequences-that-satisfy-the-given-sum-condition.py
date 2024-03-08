class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff < nums[i]:
                if 2*nums[i] < target:
                    ans += 1
            else:
                sub= bisect_right(nums, diff)
                if (sub < len(nums) and nums[sub]!= diff) or sub>=len(nums):
                    sub -= 1
                print(sub, i)
                ans += pow(2, abs(sub-i))
                
        return ans % MOD