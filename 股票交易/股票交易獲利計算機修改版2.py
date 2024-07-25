def calculate_profit_loss(buy_price, sell_price, shares):
    # 計算買入成本
    buy_cost = buy_price * shares * (1 + 0.1425 / 100)

    # 計算賣出收入
    sell_income = sell_price * shares * (1 - 0.4425 / 100)

    # 計算獲利或虧損金額
    profit_loss = sell_income - buy_cost

    # 計算獲利或虧損比例
    if buy_cost != 0:
        profit_loss_percentage = (profit_loss / buy_cost) * 100
    else:
        profit_loss_percentage = 0

    return profit_loss, profit_loss_percentage

# 主程式
if __name__ == "__main__":
    try:
        # 請使用者輸入買進價格、賣出價格和股數
        buy_price = float(input("請輸入買進價格："))
        sell_price = float(input("請輸入賣出價格："))
        shares = float(input("請輸入股數："))

        # 呼叫函數計算獲利或虧損及比例
        profit_loss, profit_loss_percentage = calculate_profit_loss(buy_price, sell_price, shares)

        # 根據結果判斷並輸出
        if profit_loss > 0:
            print(f"總獲利金額為: {profit_loss:.2f} 元")
            print(f"獲利比例為: {profit_loss_percentage:.2f}%")
        elif profit_loss < 0:
            print(f"總虧損金額為: {profit_loss:.2f} 元")
            print(f"虧損比例為: {profit_loss_percentage:.2f}%")
        else:
            print("沒有獲利也沒有虧損")

    except ValueError as e:
        print(f"錯誤: {e}")
    except Exception as e:
        print(f"程式執行出錯: {e}")
