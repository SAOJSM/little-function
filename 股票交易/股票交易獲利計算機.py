def calculate_profit_loss(buy_price, sell_price, shares):
    # 計算買入成本
    buy_cost = buy_price * shares * (1 + 0.1425 / 100)

    # 計算賣出收入
    sell_income = sell_price * shares * (1 - 0.4425 / 100)

    # 計算獲利或虧損
    profit_loss = sell_income - buy_cost

    return profit_loss

# 主程式
if __name__ == "__main__":
    # 請使用者輸入買進價格、賣出價格和股數
    buy_price = float(input("請輸入買進價格："))
    sell_price = float(input("請輸入賣出價格："))
    shares = float(input("請輸入股數："))

    # 呼叫函數計算獲利或虧損
    profit_loss = calculate_profit_loss(buy_price, sell_price, shares)

    # 根據結果判斷並輸出
    if profit_loss > 0:
        print(f"總獲利為: {profit_loss:.2f} 元")
    elif profit_loss < 0:
        print(f"總虧損為: {profit_loss:.2f} 元")
    else:
        print("沒有獲利也沒有虧損")
