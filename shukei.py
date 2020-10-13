f = open('/Users/mizumuratomoya/Desktop/pythontomo2/pdf.txt')

order = f.read()
#print(data)

#改行コードで分割してリスト化
order_list = order.splitlines()

#インデックスナンバーを取得
red_index_number = order_list.index('※ 商品名 : オーガニックルイボスティー　ティーパック　2g×30包入り　　スーパーグレード （軽）')
genmai_index_number = order_list.index('※ 商品名 : しょうが玄米ルイボスティー　ティーパック　2.5g×20包入り （軽）')
index_number_list = [red_index_number, genmai_index_number]

for index_number in index_number_list:
    #print(index_number)

    #商品名の乗っている行を取得
    name = order_list[index_number]
    #print(name)

    #個数の乗っている行を取得
    kosuu = order_list[index_number+1]
    #print(kosuu)

    #レッドの商品名の乗っている行から商品名のみをプリント
    print(name[8:21])

    #商品の個数が乗っている行から個数のみをプリント
    print(kosuu[16:18])


f.close()



#fo = open('/Users/mizumuratomoya/Desktop/pythontomo2/final.txt', 'w')
#fo.write(str(red_name[8:21]))
#fo.close()
