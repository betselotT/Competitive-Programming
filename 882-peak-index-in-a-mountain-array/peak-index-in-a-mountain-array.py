class Solution(object):
    def peakIndexInMountainArray(self, arr):
        return max(range(len(arr)), key=arr.__getitem__)