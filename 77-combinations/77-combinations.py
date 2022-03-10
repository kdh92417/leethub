class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def dfs(el, start, k):
            if k == 0:
                result.append(el[:])
                return
            
            for i in range(start, n + 1):
                el.append(i)
                dfs(el, i + 1, k - 1)
                el.pop()
        
        dfs([], 1, k)
        return result
                
        