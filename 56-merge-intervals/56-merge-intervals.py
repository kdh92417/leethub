class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        result = []

        for i, lst in enumerate(intervals):
            if not result:
                result.append(lst)

            elif lst[0] <= result[-1][-1]:
                result[-1][-1] = max(result[-1][-1], lst[-1])
            else:
                result.append(lst)

        return result