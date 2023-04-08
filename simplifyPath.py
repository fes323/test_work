class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        result = '/' + '/'.join(stack)
        if len(result) > 1 and result[-1] == '/':
            result = result[:-1]
        return print(result)


Solution.simplifyPath(Solution, path='/.home/./.../foo///')