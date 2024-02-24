class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = {}
        for rabbit in answers:
            if rabbit in counts:
                counts[rabbit] += 1
            else:
                counts[rabbit] = 1
        results = 0
        for key in counts.keys():
            count = counts[key]
            number = ((count - 1) // (key + 1)) + 1
            results += number * (key + 1)
        
        return results
        