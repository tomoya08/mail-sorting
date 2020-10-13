f = open('/Users/mizumuratomoya/Desktop/pythontomo2/pdf.txt')

order = f.read()
#print(data)

#改行コードで分割してリスト化
order_list = order.splitlines()

#インデックスナンバーを取得
red_index_number = order_list.index('※ 商品名 : オーガニックルイボスティー\u3000ティーパック\u30002g×30包入り\u3000\u3000スーパーグレード （軽） ')
orange_index_number = order_list.index('※ 商品名 : オレンジミックスルイボスティー\u3000ティーパック\u30002g×25包入り （軽） ')
apricot_index_number = order_list.index('※ 商品名 : あんずルイボスティー　ティーパック　2g×25包入り （軽）')
earlgray_index_number = order_list.index('※ 商品名 : アールグレイルイボスティー　ティーパック　2g×25包入り （軽）')
muscat_index_number = order_list.index('※ 商品名 : マスカットルイボスティー　ティーパック　2g×25包入り （軽）')
rose_index_number = order_list.index('※ 商品名 : ローズヒップルイボスティー　ティーパック　3g×20包入り （軽）')
sg_index_number = order_list.index('※ 商品名 : しょうが玄米ルイボスティー\u3000ティーパック\u30002.5g×20包入り （軽） ')
sp_index_number = order_list.index('※ 商品名 : スーパージンジャールイボスティー　ティーパック　2g×25包入り （軽）')
mojito_index_number = order_list.index('※ 商品名 : モヒートルイボスティー　ティーパック　2g×25包入り （軽）')
ainomi_index_number = order_list.index('※ 商品名 : 藍の実ルイボスティー　ティーパック　2.5g×20包入り （軽）')
soltnut_index_number = order_list.index('※ 商品名 : マカデミアナッツ（薄塩）\u3000120g （軽） ')


index_number_list = [red_index_number, orange_index_number, apricot_index_number, earlgray_index_number, muscat_index_number, rose_index_number, sg_index_number, sp_index_number, mojito_index_number, ainomi_index_number, soltnut_index_number]

for index_number in index_number_list:
    #print(index_number)

    #商品名の乗っている行を取得
    name = order_list[index_number]
    #print(name)

    #個数の乗っている行を取得
    kosuu = order_list[index_number+1]
    #print(kosuu)

    #レッドの商品名の乗っている行から商品名のみをプリント
    need_name = name[8:21]
    print(need_name)

    #商品の個数が乗っている行から個数のみをプリント
    need_kosuu = kosuu[16:18]
    print(need_kosuu)

f.close()

#fo = open('/Users/mizumuratomoya/Desktop/pythontomo2/final.txt', 'w')
#fo.write(need_name)
#fo.close()
