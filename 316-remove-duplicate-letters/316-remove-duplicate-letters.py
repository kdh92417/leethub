class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        print('sorted s : ', sorted(set(s)))
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            print(char, s.index(char), suffix)
            
            if set(s) == set(suffix):
                print('parameter : ', suffix.replace(char, ''), 'set s : ', set(s))
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''
            