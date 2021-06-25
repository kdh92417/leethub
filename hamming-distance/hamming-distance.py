class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        l = list(map(int, bin(x^y)[2:]))
        return sum(l)