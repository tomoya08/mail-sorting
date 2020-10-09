def aggregated():
    f = open('/Users/mizumuratomoya/Desktop/pythontomo2/pdf.txt', 'r')

    data = f.read()

    red = data.count('オーガニックルイボスティー')
    green = data.count('オーガニックグリーンルイボスティー')
    orange = data.count('オレンジミックスルイボスティー')
    apricot = data.count('あんずルイボスティー')
    earl = data.count('アールグレイルイボスティー')
    muscat = data.count('マスカットルイボスティー')
    rose = data.count('ローズヒップルイボスティー')
    caramel = data.count('キャラメルルイボスティー')
    yuzu = data.count('柚子しょうが')
    sg = data.count('しょうが玄米')
    sp = data.count('スーパージンジャールイボスティー')
    mojito = data.count('モヒートルイボスティー')

    #print('レッド30Ｔ' + str(red) + '個')
    #print('グリーン25Ｔ' + str(green) + '個')
    #print('オレンジ' + str(orange) + '個')
    #print('あんず' + str(apricot) + '個')
    #print('アールグレイ' + str(earl) + '個')
    #print('マスカット' + str(muscat) + '個')
    #print('ローズヒップ' + str(rose) + '個')
    #print('キャラメル' + str(caramel) + '個')
    #print('柚子しょうが' + str(yuzu) + '個')
    #print('しょうが玄米' + str(sg) + '個')
    #print('スーパージンジャールイボスティー' + str(sp) + '個')
    #print('モヒート' + str(mojito) + '個')


    f.close()

    with open('/Users/mizumuratomoya/Desktop/pythontomo2/aggregatedresult.txt', 'w') as a:
        print('レッド30Ｔ' + str(red) + '個', file=a )
        print('グリーン25Ｔ' + str(green) + '個', file=a )
        print('オレンジ' + str(orange) + '個', file=a )
        print('あんず' + str(apricot) + '個', file=a )
        print('アールグレイ' + str(earl) + '個', file=a )
        print('マスカット' + str(muscat) + '個', file=a )
        print('ローズヒップ' + str(rose) + '個', file=a )
        print('キャラメル' + str(caramel) + '個', file=a )
        print('柚子しょうが' + str(yuzu) + '個', file=a )
        print('しょうが玄米' + str(sg) + '個', file=a )
        print('スーパージンジャールイボスティー' + str(sp) + '個', file=a )
        print('モヒート' + str(mojito) + '個', file=a )

    with open('/Users/mizumuratomoya/Desktop/pythontomo2/aggregatedresult.txt') as a:
        print(a.readlines())

aggregated()
