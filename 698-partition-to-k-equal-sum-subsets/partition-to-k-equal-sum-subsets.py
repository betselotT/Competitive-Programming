class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False

        def check(i):
            if i == len(nums):    
                return True

            for j in range(k):
                if ans[j] + nums[i] <= find:
                    ans[j] += nums[i]

                    if check(i + 1):
                        return True

                    ans[j] -= nums[i]
                    if ans[j] == 0:
                        break

            return False

        find = total // k
        ans = [0] * k
        nums.sort(reverse = True)
        return check(0)