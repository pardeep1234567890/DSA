# This is the two pointers Pattern Approach 
def buy_sell_stock():
    prices =  [7, 6, 4, 3, 1]
    min_val = prices[0]
    profit = 0
    for i in range(len(prices)):
        if prices[i]<min_val :
            min_val = prices[i]
        profit = max(profit,prices[i] - min_val)
    return profit
print(buy_sell_stock())