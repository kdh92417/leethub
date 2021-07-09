class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        com = list(itertools.combinations(list(range(1, n+1)), k))
        return com