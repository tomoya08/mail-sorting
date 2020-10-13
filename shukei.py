#ファイルオープン
f = open('/Users/mizumuratomoya/Desktop/pythontomo2/pdf.txt')

order = f.read()
#print(data)

#改行コードで分割してリスト化
order_list = order.splitlines()

#レッド30Tのインデックス番号を取得
red_index = order_list.index('※ 商品名 : オーガニックルイボスティー\u3000ティーパック\u30002g×30包入り\u3000\u3000スーパーグレード （軽）')
#print(red_index)

#レッドの個数の乗っている行を取得
red_kosuu = order_list[red_index+1]
#print(red_kosuu)

#レッドの商品名の乗っている行を取得
red_name = order_list[red_index]
#print(red_name)

#レッドの商品名の乗っている行から商品名のみをプリント
print(red_name[8:21])

#商品の個数が乗っている行から個数のみをプリント
print(red_kosuu[16:18])

#-------------------------------------------------------------------------

#レッド30Tのインデックス番号を取得
genmai_index = order_list.index('※ 商品名 : しょうが玄米ルイボスティー　ティーパック　2.5g×20包入り （軽）')
#print(red_index)

#レッドの個数の乗っている行を取得
genmai_kosuu = order_list[genmai_index+1]
#print(red_kosuu)

#レッドの商品名の乗っている行を取得
genmai_name = order_list[genmai_index]
#print(red_name)

#レッドの商品名の乗っている行から商品名のみをプリント
print(genmai_name[8:21])

#商品の個数が乗っている行から個数のみをプリント
print(genmai_kosuu[16:18])




f.close()







#fo = open('/Users/mizumuratomoya/Desktop/pythontomo2/final.txt', 'w')
#fo.write(str(red_name[8:21]))
#fo.close()
