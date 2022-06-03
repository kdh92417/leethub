class Solution:
    @staticmethod
    def euclidean_distance(dot):
        result = 0
        for i in range(2):
            result += (dot[i] ** 2)
            
        return result
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = sorted([[self.euclidean_distance(p), p]  for p in points], key=lambda x: x[0])
#         for p in points:
            
#             result.append(p)
            
#             for i in range(len(result) -  1, 0, -1):
#                 j = i
#                 while j > 0:
#                     if self.euclidean_distance(result[j - 1]) > self.euclidean_distance(result[j]):
#                         result[j], result[j - 1] = result[j - 1], result[j]
#                     else:
#                         break
        
        return [p[1] for p in result[:k]]
        