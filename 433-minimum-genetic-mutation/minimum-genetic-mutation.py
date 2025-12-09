class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet=set(bank)

        visited=set()

        q=deque()
        q.append(startGene)
        level=0

        while q:
            qLen=len(q)

            for _ in range(qLen):
                curr=q.popleft()

                if curr==endGene:
                    return level

                for ch in "ACGT":
                    for i in range(len(curr)):
                        neighbor=curr[:i]+ch+curr[i+1:]
                        
                        if neighbor in bankSet and neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                
            level+=1
        return -1