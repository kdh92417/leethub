class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = itertools.permutations(nums, len(nums))
        
        return result
        
        