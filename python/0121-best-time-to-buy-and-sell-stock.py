class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0

        lowest_price = prices[0]

        for price in prices:
            if price < lowest_price:
                lowest_price = price
            best_profit = max(best_profit, price - lowest_price)

        return best_profit