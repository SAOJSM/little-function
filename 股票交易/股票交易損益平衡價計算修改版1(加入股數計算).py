def calculate_breakeven_price(buy_price, discount, shares):
    # 確保折數在合理範圍內（0.1到10之間）
    if discount < 0.1 or discount > 10:
        raise ValueError("折數必須在0.1到10之間")
