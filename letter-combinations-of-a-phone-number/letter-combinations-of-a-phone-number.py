class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        key_board = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        
        result = []
        
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for s in key_board[int(digits[i])]:
                    dfs(i+1, path+s)
        
        dfs(0, '')
        return result