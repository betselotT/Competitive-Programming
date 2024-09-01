class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        max_people = 0
        for event in s:
            if event == 'E':
                count += 1
                if count > max_people:
                    max_people = count
            elif event == 'L':
                count -= 1
                
        return max_people       
            