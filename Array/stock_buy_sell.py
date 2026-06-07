prices=[10, 7, 5, 8, 11, 9]

min_price=prices[0]
max_profit=0
for i in range(1,len(prices)):
    cost=prices[i]-min_price
    max_profit=max(max_profit,cost)
    min_price=min(min_price,prices[i])
print(min_price,max_profit)