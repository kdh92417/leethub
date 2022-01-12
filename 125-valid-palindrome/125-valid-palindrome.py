class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = [i.lower() for i in s if i.isalnum()]
        
        while len(palindrome) > 1:
            if palindrome.pop(0) != palindrome.pop():
                return False
            
        return True
            