class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        myDict = defaultdict(int)
        arr = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                num = stack.pop()
                myDict[num] = nums2[i]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            if nums1[i] in myDict:
                arr.append(myDict[nums1[i]])
            else:
                arr.append(-1)
        return arr