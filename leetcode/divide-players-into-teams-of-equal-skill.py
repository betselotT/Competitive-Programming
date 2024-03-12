class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        arr = []
        left, right = 0, len(skill) - 1
        ans = 0
        for _ in range(len(skill) // 2):
            arr.append((skill[left], skill[right]))
            left += 1
            right -= 1
        for i in range(1, len(arr)):
            new = arr[i][0] + arr[i][1]
            if arr[i - 1][0] + arr[i - 1][1] != new:
                return -1
        for i in range(len(arr)):
            temp = arr[i][0] * arr[i][1]
            ans += temp
        return ans