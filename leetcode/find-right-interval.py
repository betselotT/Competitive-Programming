class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        myDict = defaultdict(int)
        first = []
        second = []
        arr = []
        for i in intervals:
            first.append(i[0])
            second.append(i[1])
        for i in range(len(first)):
            myDict[first[i]] = i
        first.sort() 
        for i in range(len(intervals)):
            if second[i] not in first and max(first) < second[i]:
                arr.append(-1)
            else:
                ans = bisect_left(first, second[i])
                num = first[ans]
                arr.append(myDict[num])
        return arr