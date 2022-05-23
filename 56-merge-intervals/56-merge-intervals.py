class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for lst in sorted(intervals, key=lambda x: x[0]):
            print(lst)
            if result and result[-1][-1] >= lst[0]:
                result[-1][-1] = max(result[-1][-1], lst[-1])
            else:
                result.append(lst)

        return result