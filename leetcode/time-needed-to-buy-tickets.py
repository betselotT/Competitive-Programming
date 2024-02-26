class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([i for i in range(len(tickets))])
        time = 0
        
        while queue:
            for _ in range(len(queue)):
                buyer = queue.popleft()
                tickets[buyer] -= 1

                if tickets[buyer] >= 1:
                    queue.append(buyer)
                time += 1

                if tickets[k] == 0:
                    return time