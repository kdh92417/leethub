class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(el, start):
            if sum(el) > target:
                return
            elif sum(el) == target:
                result.append(el[:])
                return
                
            for i in range(start, len(candidates)):
                el.append(candidates[i])
                dfs(el, i)
                el.pop()
                
        dfs([], 0)
        
        return result