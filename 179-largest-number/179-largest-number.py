class Solution:
    @staticmethod
    def to_swap(n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    def largestNumber(self, nums: List[int]) -> str:
        
        for i in range(1, len(nums)):
            
            for j in range(i, 0, -1):
                if self.to_swap(nums[j - 1], nums[j]):
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    
        return str(int(''.join(map(str, nums))))