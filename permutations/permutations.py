class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_lst = []
        
        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_lst[:])
                return
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_lst.append(e)
                dfs(next_elements)
                prev_lst.pop()
        
        dfs(nums)
        
        return result
            
                