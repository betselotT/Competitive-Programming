class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pos = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                pos = i
                break
               
        for r in range(pos+1, len(nums)):
            if nums[r] == 1:
                if r - i -1 >= k:
                    i = r
                    continue
                else:
                    return False
        return True