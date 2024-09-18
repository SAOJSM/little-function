def calculate_average_cost(buy_price, shares, discount):
    # 確保折數在合理範圍內（0.1到10之間）
    if discount < 0.1 or discount > 10:
        raise ValueError("折數必須在0.1到10之間")

    # 計算買入成本
    buy_cost = buy_price * shares * (1 + 0.1425 / 100 * (discount / 10))

    # 計算均價
    average_cost = buy_cost / shares

    return buy_cost, average_cost

# 主程式
if __name__ == "__main__":
    try:
        # 請使用者輸入買進價格、股數和折數
        buy_price = float(input("請輸入買進價格："))
        shares = float(input("請輸入股數："))
        discount = float(input("請輸入折數（0.1到10之間）："))

        # 呼叫函數計算均價和買入成本
        buy_cost, average_cost = calculate_average_cost(buy_price, shares, discount)

        # 輸出結果
        print(f"買入成本為: {buy_cost:.2f} 元")
        print(f"買進均價為: {average_cost:.2f} 元")

    except ValueError as e:
        print(f"錯誤: {e}")
    except Exception as e:
        print(f"程式執行出錯: {e}")
