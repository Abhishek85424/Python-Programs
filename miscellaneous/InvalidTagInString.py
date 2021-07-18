import sys
prices =[7,1,5,3,6,4]
start = 0
end = 1
min_price = sys.maxsize
max_profit = 0

for index, value in enumerate(prices):
    if value < min_price:
        min_price = value
    elif value - min_price > max_profit:
        max_profit = value - min_price
print(max_profit)