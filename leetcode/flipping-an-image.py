class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left = 0
            right = len(row) - 1
            while left <= right:
                temp = row[left]
                row[left] = row[right]
                row[right] = temp
                left += 1
                right -= 1
        for i in image:
            for j in range(len(i)):
                i[j] = 1 - i[j]
        return image