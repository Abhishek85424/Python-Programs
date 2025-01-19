"""
calculates the maximum profit that can be achieved by buying and selling a stock given a list of prices
, where each price represents the stock price on a particular day.
"""
import sys

prices = [7, 1, 5, 3, 6, 4]
min_price = sys.maxsize
max_profit = 0

print(2**31)
print(sys.maxsize)

for index, current_price in enumerate(prices):
    if current_price < min_price:
        min_price = current_price
    elif current_price - min_price > max_profit:
        max_profit = current_price - min_price
print(max_profit)
