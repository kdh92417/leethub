class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

        return result
