class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c_nums = collections.Counter(nums1)
        result = set()
        for num in nums2:
            if c_nums[num] > 0:
                result.add(num)
        return result