class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = [i.lower() for i in s if i.isalnum()]
        
        LEN = len(palindrome)
        for i in range(LEN // 2):
            if palindrome[i] != palindrome[-i - 1]:
                return False
        return True
            