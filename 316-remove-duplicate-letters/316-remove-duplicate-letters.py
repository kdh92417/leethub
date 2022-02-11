class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c, stack = collections.Counter(s), []
        seen = set()
        
        for char in s:
            c[char] -= 1
            print(stack, char)
            if char in seen:
                print('continue')
                continue
            
            while stack and char < stack[-1] and c[stack[-1]] > 0:
                seen.remove(stack.pop())
                
            
            seen.add(char)
            stack.append(char)
            
        return ''.join(stack)