# 秒数を入力として受け取る
seconds = int(input("秒数を入力してください:"))

# 秒数を分に変換
minutes = seconds // 60

# 余りの秒数を計算
remaining_seconds = seconds % 60

# 結果を表示
print(f"{seconds} 秒は {minutes} 分 {remaining_seconds} 秒です。")
