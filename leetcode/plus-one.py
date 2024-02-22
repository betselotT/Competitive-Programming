class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new = int("".join(map(str, digits)))
        new += 1
        newList = [int(digit) for digit in str(new)]
        return newList