class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(idx, path):
            if len(path) == len(digits):
                res.append(path)
                return
            
            for i in range(idx, len(digits)):
                for letter in key_pad[digits[i]]:
                    dfs(i + 1, path + letter)
                    
        if not digits:
            return []
        
        key_pad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
         
        res = []
        dfs(0, "")
        
        return res
            
        
        