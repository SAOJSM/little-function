# 定義一個函數來執行加法
def add(x, y):
    return x + y

# 定義一個函數來執行減法
def subtract(x, y):
    return x - y

# 定義一個函數來執行乘法
def multiply(x, y):
    return x * y

# 定義一個函數來執行除法
def divide(x, y):
    if y == 0:
        return "不能除以零！"
    else:
        return x / y

# 這是主程式
while True:
    # 顯示選項給用戶
    print("選擇運算：")
    print("1. 加")
    print("2. 減")
    print("3. 乘")
    print("4. 除")
    print("5. 退出")

    # 輸入選項
    choice = input("輸入你的選擇（1/2/3/4/5）：")

    # 檢查用戶選擇
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("輸入第一個數字："))
        num2 = float(input("輸入第二個數字："))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    
    elif choice == '5':
        print("退出計算機")
        break
    
    else:
        print("無效的輸入")
