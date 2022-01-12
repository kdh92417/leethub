class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = [i.lower() for i in s if i.isalnum()]
        
        return palindrome == palindrome[::-1]
            