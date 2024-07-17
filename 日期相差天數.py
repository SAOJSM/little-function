from datetime import datetime

def days_between_dates(date1, date2):
    # 將日期字串轉換成 datetime 物件
    date1_obj = datetime.strptime(date1, '%Y-%m-%d')
    date2_obj = datetime.strptime(date2, '%Y-%m-%d')

    # 計算日期差距
    delta = date2_obj - date1_obj

    # 取得差距的天數
    return delta.days

# 主程式
if __name__ == "__main__":
    # 輸入日期
    date_str1 = input("輸入第一個日期（YYYY-MM-DD）：")
    date_str2 = input("輸入第二個日期（YYYY-MM-DD）：")

    # 呼叫函數計算天數差距並輸出結果
    try:
        days_diff = days_between_dates(date_str1, date_str2)
        print(f"兩個日期之間相差 {days_diff} 天")
    except ValueError as e:
        print("日期格式錯誤，請輸入正確的日期格式（YYYY-MM-DD）")
