class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit: int = 0

        # Initialise buy and sell days
        buy: int = 0
        sell: int = 0

        # Iterate over prices until end of list
        while sell < len(prices):
            # If we buy at a higher or equal price than we sell, set buy date to sell and increment sell date
            if prices[buy] >= prices[sell]:
                buy = sell
                sell += 1
            else:
                max_profit = max(max_profit, prices[sell] - prices[buy])
                sell += 1
        return max_profit