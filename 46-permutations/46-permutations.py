class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums or len(nums) == 1:
            return [nums]
        
        def dfs(per, remain_nums):
            
            if len(per) == len(nums):
                result.append(per)
                return
            
            for i in range(len(remain_nums)):
                dfs(per+[remain_nums[i]], remain_nums[:i] + remain_nums[i+1:])
        
        
        result = []
        dfs([], nums)
        
        return result