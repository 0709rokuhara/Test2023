import json

#条件に合致するデータを格納
hoge=[]
#withでファイルのオープンとクローズを自動処理
with open('catalog.json', encoding='utf-8') as file:
    #jsonファイルを変数xに格納
    x=json.load(file)
    #xの各要素に対してループ
    for j_value in x:
        try:
            if j_value["name"]=="jacket":
                #名前がjacketのとき、priceの値を整数にしてyに価格を代入、hogeにappend
                y=int(j_value["price"])
                hoge.append(y)
        #エラー処理
        except ValueError:
            continue
#リストの長さ＝個数
print(len(hoge))
#リストのMAX値
print(max(hoge))
#リストのMIN値
print(min(hoge))        