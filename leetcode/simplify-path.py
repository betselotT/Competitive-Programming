class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        new = path.split('/')
        for i in new:
            if i == '..':
                if not stack:
                    continue
                else:
                    stack.pop()
            elif i == '':
                continue
            elif i != '.' and i[0] != '/':
                stack.append(i)
            else:
                continue
        return '/' + '/'.join(stack)