class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        print('========= sorted s : ', sorted(set(s)), ' || s :', s)
        
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            print('char: ' , char, ' || suffix : ', suffix, ' || set(s) : ', set(s))
            
            if set(s) == set(suffix):
                print('recursice Char: ', char)
                result = char + self.removeDuplicateLetters(suffix.replace(char, ''))
                return result
        return ''
            