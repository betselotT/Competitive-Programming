class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        n, m = len(nums1), len(nums2)
        if n >= m:
            for num in nums1:
                if num in nums2:
                    arr.append(num)
                    nums2.remove(num)
        if m > n:
            for num in nums2:
                if num in nums1:
                    arr.append(num)
                    nums1.remove(num)
        return arr
