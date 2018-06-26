def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    money = 0
    end = len(prices)
    for i in range(end):
        price = max(prices[i:])
        if money < (price - prices[i]):
            money = (price - prices[i])
    return money

prices = [7,6,4,3,1]
# prices = [7, 1, 5, 3, 6, 4]
res = maxProfit(prices)
print(res)
