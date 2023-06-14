#エラーメッセージ表示に使用
import sys
#合計値格納用
nums=[]

#ファイルを開く
with open('data.txt', encoding='utf-8') as file:
    for number in file.readlines():
        try:
            #整数への変換を試みる
            num = int(number)
        except ValueError as e:
            #エラー処理、表示する
            print(e, file=sys.stderr)
            #失敗したら次の行の処理
            continue

        #整数に変換できたものを追加していく
        nums.append(num)

    print(sum(nums))
