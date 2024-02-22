class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i == './':
                continue
            if i == '../':
                if not stack:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(i)
        return len(stack)