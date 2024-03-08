class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        arr = list(set(nums1) & set(nums2))
        if arr == []:
            return -1
        else:
            return min(arr)