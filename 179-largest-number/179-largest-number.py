class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = sorted(list(map(str, nums)), key=lambda x: x*9, reverse=True)
        
        return str(int(''.join(sorted_nums)))