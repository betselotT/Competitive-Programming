class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        gpivot = []
        lpivot = []
        mpivot = []
        arr = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                lpivot.append(nums[i])
            elif nums[i] > pivot:
                gpivot.append(nums[i])
            else:
                mpivot.append(nums[i])
        arr = lpivot + mpivot + gpivot
        return arr