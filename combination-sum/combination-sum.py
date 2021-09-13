class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(csum, index, path):
            # Termination Conditions
            if csum < 0:
                return
            elif csum == 0:
                result.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
            
        dfs(target, 0, [])
        
        return result