class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        max_p = 0

        for end in range(0,len(prices)):
            profit = prices[end] - prices[start]

            while prices[end] - prices[start] < 0:
                start += 1
            max_p = max(profit, max_p)
        return max_p