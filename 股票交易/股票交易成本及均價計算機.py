def calculate_average_cost(buy_price, shares):
    # 計算買入成本
    buy_cost = buy_price * shares * (1 + 0.1425 / 100)

    # 計算均價
    average_cost = buy_cost / shares

    return buy_cost, average_cost

# 主程式
if __name__ == "__main__":
    try:
        # 請使用者輸入買進價格和股數
        buy_price = float(input("請輸入買進價格："))
        shares = float(input("請輸入股數："))

        # 呼叫函數計算買入成本和均價
        buy_cost, average_cost = calculate_average_cost(buy_price, shares)

        # 輸出買入成本和均價
        print(f"買入成本為: {buy_cost:.2f} 元")
        print(f"買進均價為: {average_cost:.2f} 元")

    except ValueError as e:
        print(f"錯誤: {e}")
    except Exception as e:
        print(f"程式執行出錯: {e}")