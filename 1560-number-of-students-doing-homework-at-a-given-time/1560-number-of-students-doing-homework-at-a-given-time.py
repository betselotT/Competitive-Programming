class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        cnt = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                cnt += 1
        return cnt