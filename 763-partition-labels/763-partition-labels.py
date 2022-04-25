class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_collection = { char: idx for idx, char in enumerate(s) }
        
        result = []
        left, right = 0, 0
        
        for i, char in enumerate(s):
            
            right = max(right, s_collection[char])
            
            if i == right:
                result.append(right - left + 1)
                left = right + 1
        
        return result