class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(path, lst):
            
            result.append(path)
            
            for i in range(len(lst)):
                dfs(path + [lst[i]], lst[i+1:])
            
            return
        
        dfs([], nums)
        
        return result