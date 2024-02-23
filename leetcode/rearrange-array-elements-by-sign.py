class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        arr = []
        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        for i, j in zip(pos, neg):
            arr.append(i)
            arr.append(j)
        return arr