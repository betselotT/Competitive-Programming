class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        arr = {}
        newArr = []
        size, end = 0, 0
        for i, letter in enumerate(s):
            arr[letter] = i
        for i, letter in enumerate(s):
            size += 1
            end = max(arr[letter], end)
            if i == end:
                newArr.append(size)
                size = 0
        return newArr