class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        res = []
        currpos = 1
        currneg = 0

        j = 0

        while(True and len(nums) >= 2 and j < len(nums)-1):
            if nums[j] < nums[j+1]:
                res.append(nums[j])
                currpos,currneg = 0, 1
                break

            if nums[j] > nums[j+1]:
                res.append(nums[j])
                currpos,currneg = 1, 0
                break
            j += 1

        for i in range(j+1,len(nums)-1):
            if currpos == 1:
                if nums[i] < nums[i+1]:
                    res.append(nums[i])
                    currpos,currneg = 0,1
            elif currneg == 1:
                if nums[i] > nums[i+1]:
                    res.append(nums[i])
                    currpos,currneg = 1,0
    
        if currpos == 1:
            if res and nums[-1] < res[-1]:
                res.append(nums[-1])
        
        if currneg == 1:
            if res and nums[-1] > res[-1]:
                res.append(nums[-1])

        if len(res) == 0:
            return 1
        return len(res)
        