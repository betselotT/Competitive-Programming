class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] - ans <= 0: 
                continue
            else: 
                ans += 1
        return ans