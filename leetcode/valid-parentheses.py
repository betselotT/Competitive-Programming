class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
                continue
            if stack and i == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and i == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
        return not stack