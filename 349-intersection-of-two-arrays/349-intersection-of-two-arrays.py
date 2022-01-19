class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums1.sort()
        
        for n2 in nums2:
            n_idx = bisect.bisect_left(nums1, n2)
            
            if len(nums1) > n_idx and nums1[n_idx] == n2:
                result.add(n2)
        return result