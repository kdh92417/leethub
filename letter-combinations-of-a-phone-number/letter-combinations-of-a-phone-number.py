from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return digits
        
        dig = {
            2 : ['a', 'b', 'c'],
            3 : ['d', 'e', 'f'],
            4 : ['g', 'h', 'i'],
            5 : ['j', 'k', 'l'],
            6 : ['m', 'n', 'o'],
            7 : ['p', 'q', 'r', 's'],
            8 : ['t', 'u', 'v'],
            9 : ['w', 'x', 'y', 'z']
        }
        
        if len(digits) < 2:
            return dig[int(digits)]
        
        com = product(*[dig[int(i)] for i in digits])
        result = [''.join(c) for c in com]
        return result