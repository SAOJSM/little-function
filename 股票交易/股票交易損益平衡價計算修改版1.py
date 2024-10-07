def calculate_breakeven_price(buy_price, discount, shares):
    # 確保折數在合理範圍內（0.1到10之間）
    if discount < 0.1 or discount > 10:
        raise ValueError("折數必須在0.1到10之間")

    # 計算手續費
    commission_fee = (0.1425 / 100 * 2 * (discount / 10)) + (0.15 / 100)

    # 計算損益平衡價
    breakeven_price = buy_price * (1 + commission_fee)

    return breakeven_price
