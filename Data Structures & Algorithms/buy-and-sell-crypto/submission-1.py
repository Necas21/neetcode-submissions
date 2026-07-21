class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit: int = 0

        # If prices is length 1, return 0
        if len(prices) == 1:
            return max_profit

        # Iterate over prices as the sell price
        for sell_date in range(1, len(prices)):
            # Get the minimum buy price up to sell_date
            min_buy: int = min(prices[:sell_date])
            # The highest profit possible by selling on sell_date
            profit: int = prices[sell_date] - min_buy
            # Update max_profit with the higher of max_profit and profit
            max_profit = max(max_profit, profit)
        
        return max_profit