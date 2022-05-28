class Solution:
    @staticmethod
    def to_swap(n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    def largestNumber(self, nums: List[int]) -> str:
        
        for i in range(1, len(nums)):
            
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
                    
        return str(int(''.join(map(str, nums))))