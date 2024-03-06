class TimeMap:

    def __init__(self):
        self.myDict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myDict:
            self.myDict[key] = []
        self.myDict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        values = self.myDict.get(key, [])
        low, high = 0, len(values) - 1
        while low <= high:
            mid = (low + high) // 2
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)