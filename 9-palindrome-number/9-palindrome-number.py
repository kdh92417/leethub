class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = collections.deque([string for string in str(x)])
        
        while len(x) > 1:
            if x.popleft() != x.pop():
                return False
        return True
        