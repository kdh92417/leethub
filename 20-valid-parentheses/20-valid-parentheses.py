class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1:
            return False
        
        bracket = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        
        stack = []
        
        for b in s:
            
            if b in bracket:
                stack.append(bracket[b])
            elif b not in stack:
                return False

            if stack and stack[-1] == b:
                stack.pop()
                
        return False if stack else True