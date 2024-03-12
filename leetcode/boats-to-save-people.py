class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        arr = []
        while left <= right:
            if people[right] + people[left] > limit:
                arr.append((people[right]))
                right -= 1
            else:
                arr.append((people[left], people[right]))
                left += 1
                right -= 1
        return len(arr)