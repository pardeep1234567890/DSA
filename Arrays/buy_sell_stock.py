# this is the brute force approach
# def buy_sell():
#     prices = [7,1,5,3,6,4]
#     max_profit = 0
#     for i in range(len(prices)):
#         for j in range(i+1,len(prices)):
#             new_max_profit = prices[j]-prices[i]
#             if new_max_profit>max_profit:
#                 max_profit = new_max_profit
#     return max_profit    
        
# print(buy_sell())

# def buy_sell():
#     prices = [7,1,5,3,6,4]
#     max_profit = 0
#     min_price = prices[0]
#     for i in range(len(prices)):
#         if prices[i] < min_price:
#             min_price = prices[i]
        
#         profit = prices[i] - min_price
#         if profit > max_profit:
#             max_profit = profit 
#     return max_profit             
# print(buy_sell())

def buy_sell():
    prices = [7,1,5,3,6,4]
    max_profit = 0
    min_price = prices[0] # we write it here because it tracks the history here if we write inside the loop then it will update according to loop
    for item in prices:
        # we do them seperately because we have to both of them without any condition like fing both min_price and max_profit
        if item < min_price:   
            min_price = item
        
        profit = item - min_price
        if profit > max_profit:
            max_profit = profit 
    return max_profit             
print(buy_sell())